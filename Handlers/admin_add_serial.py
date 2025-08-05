from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from Database.load_serials import load_serials_db
from Database.add_serial import add_serial_db
from Database.select_serial_kino_id import select_serial_id_db
from States.admin_add_states import AdminSerialAdd, AdminState
from Keyboards.admin_keyboards import admin_keyboard
from Keyboards.select_serials_kb import get_serials_keyboard
from Keyboards.orqaga import orqaga

router = Router()

@router.message(AdminSerialAdd.serial)
async def admin_add_serial_handler(message: Message, state: FSMContext):
    serial_name = message.text.strip().lower()  # bo‘sh joylarni olib tashlaydi va kichik harfga o‘tkazadi

    if serial_name == '🔙 orqaga'.lower():  # moslashtirilgan solishtirish
        await message.answer("Asosiy menu :", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
        return  # boshqa kodlar bajarilmasligi uchun

    # pastda faqat serial bo‘lsa ishlaydi
    serial_info = load_serials_db(message.text)  # asl nom bilan yuklab olamiz
    await message.answer("Serial qismi idsini oralig'ini kiriting, Masalan: 1 100", reply_markup=orqaga)
    await state.set_state(AdminSerialAdd.qism_id)
    await state.update_data(serial_info=serial_info)
    await state.update_data(videos=[])
    await state.update_data(seconds=[])


@router.message(AdminSerialAdd.qism_id)
async def admin_add_qismid_handler(message: Message, state: FSMContext):
    qism_id = message.text
    if qism_id == '🔙 orqaga':
        await state.set_state(AdminSerialAdd.serial)
        await message.answer("Qaysi serialga qo'shmoqchisiz", reply_markup=get_serials_keyboard())
        return

    await message.answer("Serialning faslini kiriting")
    await state.set_state(AdminSerialAdd.fasl)
    await state.update_data(qism_ids=qism_id.split())


@router.message(AdminSerialAdd.fasl)
async def admin_add_fasl_handler(message: Message, state: FSMContext):
    fasl = message.text
    if fasl == '🔙 orqaga':
        await state.set_state(AdminSerialAdd.qism_id)
        await message.answer("Serial qismi idsini kiriting")
        return
    if fasl.isdigit():
        await message.answer("Serialni qismini oralig'ini kiriting, Masalan: 1 100")
        await state.set_state(AdminSerialAdd.qism)
        await state.update_data(serial_fasl=fasl)
    else:
        await message.answer("Iltimos faslni raqamda kiriting")


@router.message(AdminSerialAdd.qism)
async def admin_add_qism_handler(message: Message, state: FSMContext):
    qism = message.text
    if qism == '🔙 orqaga':
        await state.set_state(AdminSerialAdd.fasl)
        await message.answer("Serialning faslini kiriting")
        return

    await message.answer("Videolarni jo'nating, toxtatish uchun /stop comandasini yozing")
    await state.set_state(AdminSerialAdd.video)
    await state.update_data(serial_qisms=qism.split())


@router.message(Command("stop"))
async def admin_add_all_handler(message: Message, state: FSMContext):
    await message.answer("Videolar saqlanmoqda...")
    try:
        data = await state.get_data()
        add_serial_db(data)
        await message.answer("Serial qo'shildi!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    except:
        await message.answer("Xatolik yuzaga keldi!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)


@router.message(AdminSerialAdd.video)
async def admin_add_video_handler(message: Message, state: FSMContext):
    if message.text == '🔙 orqaga':
        await state.set_state(AdminSerialAdd.qism)
        await message.answer("Serialni qismini kiriting")
        return

    video = message.video
    if video:
        data = await state.get_data()
        videos = data.get("videos", [])
        seconds = data.get("seconds", [])
        videos.append(video.file_id)
        seconds.append(video.duration)
        await state.update_data(videos=videos, seconds=seconds)
    else:
        await message.answer("Iltimos, video yuboring")





    #
    # if video:
    #     await state.update_data(video_id=video.file_id)
    #     duration_sec = video.duration
    #     await state.update_data(second=duration_sec)
    #     data = await state.get_data()
    #     add_serial_db(data)
    #     await message.answer("Serial qo'shildi!", reply_markup=admin_keyboard)
    #     await state.set_state(AdminState.add_remove)
    # else:
    #     await message.answer("Iltimos video yuboring...")