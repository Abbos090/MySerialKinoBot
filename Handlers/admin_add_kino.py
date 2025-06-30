from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.admin_add_states import AdminKinoAdd, AdminState
from Database.add_kino import add_kino_db
from Database.select_serial_kino_id import select_kino_id_db
from Keyboards.admin_keyboards import admin_keyboard

router = Router()

@router.message(AdminKinoAdd.kino_id)
async def admin_kino_add_id_handler(message: Message, state: FSMContext):
    kino_id = message.text
    if kino_id == '🔙 orqaga':
        await message.answer("Tanlang", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
        return
    if kino_id.isdigit():
        if select_kino_id_db(int(kino_id)):
            await message.answer("Bu idli kino sizda mavjud. Iltimos boshqa id kiriting")
        else:
            await message.answer("Kinoni nomini kiriting")
            await state.update_data(id=kino_id)
            await state.set_state(AdminKinoAdd.kino_name)
    else:
        await message.answer("Iltimos is raqam bo'lsin")

@router.message(AdminKinoAdd.kino_name)
async def admin_kino_add_name_handler(message: Message, state: FSMContext):
    name = message.text
    await message.answer("Kino tilini kiriting")
    await state.update_data(name=name)
    await state.set_state(AdminKinoAdd.kino_language)

@router.message(AdminKinoAdd.kino_language)
async def admin_kino_add_language_handler(message: Message, state: FSMContext):
    language = message.text
    await message.answer("Kino ishlab chiqarilgan yilini kiriting")
    await state.update_data(language=language)
    await state.set_state(AdminKinoAdd.kino_year)


@router.message(AdminKinoAdd.kino_year)
async def admin_kino_add_year_handler(message: Message, state: FSMContext):
    year = message.text
    if year.isdigit():
        await message.answer("Kino janrini kiriting")
        await state.update_data(year=year)
        await state.set_state(AdminKinoAdd.kino_janr)
    else:
        await message.answer("IIltimos yil raqam bo'lsin")

@router.message(AdminKinoAdd.kino_janr)
async def admin_kino_add_janr_handler(message: Message, state: FSMContext):
    janr = message.text
    await message.answer("Kino qismini kiriting")
    await state.update_data(janr=janr)
    await state.set_state(AdminKinoAdd.kino_qism)


@router.message(AdminKinoAdd.kino_qism)
async def admin_kino_add_qism_handler(message: Message, state: FSMContext):
    qism = message.text
    if qism.isdigit():
        await message.answer("Video jo'nating")
        await state.update_data(qism=qism)
        await state.set_state(AdminKinoAdd.vide_id)
    else:
        await message.answer("Iltimis kino qismi raqam bo'lsin")

@router.message(AdminKinoAdd.vide_id)
async def admin_kino_add_video_handler(message: Message, state: FSMContext):
    video = message.video
    if video:
        await state.update_data(video_id=video.file_id)
        duration_second = int(video.duration)
        await state.update_data(second=duration_second)
        data = await state.get_data()
        add_kino_db(data)
        await message.answer("Kino qabul qilindi!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer("Iltimos video yuboring")

