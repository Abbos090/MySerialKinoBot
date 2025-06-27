from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from States.admin_add_states import AdminCreateSerialState, AdminState
from Database.create_serial import create_serial_db
from Keyboards.admin_keyboards import admin_keyboard

router = Router()

@router.message(AdminCreateSerialState.serial_id)
async def admin_cr_id_handler(message: Message, state: FSMContext):
    serial_id = message.text
    if serial_id == '🔙 orqaga':
        await message.answer("Tanlang", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
        return
    if serial_id.isdigit():
        await message.answer("Serial nomini kiriting")
        await state.set_state(AdminCreateSerialState.serial_name)
        await state.update_data(serial_id=serial_id)
    else:
        await message.answer("Iltimos id raqam bo'lsin")

@router.message(AdminCreateSerialState.serial_name)
async def admin_cr_name_handler(message: Message, state: FSMContext):
    serial_name = message.text
    await message.answer("Serial tilini kiriting")
    await state.set_state(AdminCreateSerialState.serial_language)
    await state.update_data(serial_name=serial_name)

@router.message(AdminCreateSerialState.serial_language)
async def admin_cr_language_handler(message: Message, state: FSMContext):
    language = message.text
    await message.answer("Serial janrini kiriting")
    await state.set_state(AdminCreateSerialState.serial_janr)
    await state.update_data(serial_language=language)

@router.message(AdminCreateSerialState.serial_janr)
async def admin_cr_janr_handler(message: Message, state: FSMContext):
    janr = message.text
    await message.answer("Serial yilini kiriting")
    await state.set_state(AdminCreateSerialState.serial_year)
    await state.update_data(serial_janr=janr)


@router.message(AdminCreateSerialState.serial_year)
async def admin_cr_year_handler(message: Message, state: FSMContext):
    year = message.text
    if year.isdigit():
        try:
            await state.update_data(serial_year=year)
            data = await state.get_data()
            create_serial_db(data)

            await message.answer("Serial yaratildi!", reply_markup=admin_keyboard)
            await state.set_state(AdminState.add_remove)
        except:
            await message.answer("Xatolik, Serial yaratib bo'lmadi")
    else:
        await message.answer("Iltimos yilni sonda kiriting")

