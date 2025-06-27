from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Keyboards.admin_keyboards import admin_keyboard
from States.admin_delete_states import AdminDeleteSerial, AdminDeleteSerialQism, AdminDeleteKino, AdminDelete
from States.admin_add_states import AdminState
from Keyboards.delete_serial_kino_kb import delete_serial_kino
from Database.delete_serials_db import delete_serials_db, delete_serial_qism_db, delete_kino_db

router = Router()

@router.message(AdminDeleteSerial.serial_name)
async def delete_serial_handler(message: Message, state: FSMContext):
    serial_id = message.text
    if serial_id == "🔙 orqaga":
        await state.set_state(AdminDelete.serial_kino)
        await message.answer("Qaysi categoryni o'chirmoqchisiz", reply_markup=delete_serial_kino)
        return

    deleted = delete_serials_db(serial_id)
    if deleted > 0:
        await message.answer("Serial o'chirildi", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer("Bunday id li serial topilmadi")


@router.message(AdminDeleteSerialQism.serial_qism_id)
async def delete_serial_qism_id_handler(message: Message, state: FSMContext):
    serial_qism_id = message.text
    if serial_qism_id == "🔙 orqaga":
        await state.set_state(AdminDelete.serial_kino)
        await message.answer("Qaysi categoryni o'chirmoqchisiz", reply_markup=delete_serial_kino)
        return

    deleted = delete_serial_qism_db(serial_qism_id)
    if deleted > 0:
        await message.answer("Serial qismi o'chirildi", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer("Bunday id li serial topilmadi")


@router.message(AdminDeleteKino.kino_id)
async def delete_kino_id_handler(message: Message, state: FSMContext):
    kino_id = message.text
    if kino_id == "🔙 orqaga":
        await state.set_state(AdminDelete.serial_kino)
        await message.answer("Qaysi categoryni o'chirmoqchisiz", reply_markup=delete_serial_kino)
        return

    deleted = delete_kino_db(kino_id)
    if deleted > 0:
        await message.answer("Kino o'chirildi", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer("Bunday id li kino topilmadi")