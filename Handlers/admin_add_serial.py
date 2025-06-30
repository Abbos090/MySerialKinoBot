from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Database.load_serials import load_serials_db
from Database.add_serial import add_serial_db
from Database.select_serial_kino_id import select_serial_id_db
from States.admin_add_states import AdminSerialAdd, AdminState
from Keyboards.admin_keyboards import admin_keyboard

router = Router()

@router.message(AdminSerialAdd.serial)
async def admin_add_serial_handler(message: Message, state: FSMContext):
    serial_name = message.text.strip().lower()  # bo‘sh joylarni olib tashlaydi va kichik harfga o‘tkazadi

    if serial_name == '🔙 orqaga'.lower():  # moslashtirilgan solishtirish
        await message.answer("Tanlang", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
        return  # boshqa kodlar bajarilmasligi uchun

    # pastda faqat serial bo‘lsa ishlaydi
    serial_info = load_serials_db(message.text)  # asl nom bilan yuklab olamiz
    await message.answer("Serial qismi idsini kiriting")
    await state.set_state(AdminSerialAdd.qism_id)
    await state.update_data(serial_info=serial_info)


@router.message(AdminSerialAdd.qism_id)
async def admin_add_qismid_handler(message: Message, state: FSMContext):
    qism_id = message.text
    if qism_id.isdigit():
        if select_serial_id_db(int(qism_id)):
            await message.answer("Bu idli kino sizda mavjud. Iltimos boshqa id kiriting")
        else:
            await message.answer("Serialning faslini kiriting")
            await state.set_state(AdminSerialAdd.fasl)
            await state.update_data(qism_id=qism_id)
    else:
        await message.answer("Iltimos qismni id sini raqamda kiriting")

@router.message(AdminSerialAdd.fasl)
async def admin_add_fasl_handler(message: Message, state: FSMContext):
    fasl = message.text
    if fasl.isdigit():
        await message.answer("Serialni qismini kiriting")
        await state.set_state(AdminSerialAdd.qism)
        await state.update_data(serial_fasl=fasl)
    else:
        await message.answer("Iltimos faslni raqamda kiriting")

@router.message(AdminSerialAdd.qism)
async def admin_add_qism_handler(message: Message, state: FSMContext):
    qism = message.text
    if qism.isdigit():
        await message.answer("Video jo'nating")
        await state.set_state(AdminSerialAdd.video)
        await state.update_data(serial_qism=qism)
    else:
        await message.answer("Iltimos qism raqam bo'lsin")

@router.message(AdminSerialAdd.video)
async def admin_add_video_handler(message: Message, state: FSMContext):
    video = message.video
    if video:
        await state.update_data(video_id=video.file_id)
        duration_sec = video.duration
        await state.update_data(second=duration_sec)
        data = await state.get_data()
        add_serial_db(data)
        await message.answer("Serial qo'shildi!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer("Iltimos video yuboring...")