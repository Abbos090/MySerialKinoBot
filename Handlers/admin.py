from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import ADMINS
from States.admin_add_states import AdminState, AdminCreateSerialState, AdminSerialAdd, AdminKinoAdd
from States.admin_delete_states import AdminDelete, AdminDeleteSerial, AdminDeleteKino, AdminDeleteSerialQism
from Keyboards.admin_keyboards import admin_keyboard
from Keyboards.select_serials_kb import get_serials_keyboard
from Keyboards.delete_serial_kino_kb import delete_serial_kino
from Keyboards.orqaga import orqaga
from Keyboards.user_kino_serial import user_choose_kb


router = Router()

@router.message(CommandStart() or AdminState.add_remove)
async def admin_start_handler(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Xush kelibsiz admin!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer(f"Xush kelibsiz {message.from_user.full_name}")
        await message.answer("Kino kodini kiriting yoki tanlang :", reply_markup=user_choose_kb)

@router.message(AdminState.add_remove)
async def admin_add_remove_handler(message: Message, state: FSMContext):
    if message.text == "Serial yaratish":
        await message.answer("Yaratmoqchi bo'lgan serialingizni idsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminCreateSerialState.serial_id)
    elif message.text == "Serial qo'shish":
        await message.answer("Qaysi serialga qo'shmoqchisiz", reply_markup=get_serials_keyboard())
        await state.set_state(AdminSerialAdd.serial)
    elif message.text == "Kino qo'shish":
        await message.answer("Qo'shmoqchi bo'lgan kinoingizni idsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminKinoAdd.kino_id)
    elif message.text == "O'chirish":
        await message.answer("Qaysi categoryni o'chirmoqchisiz", reply_markup=delete_serial_kino)
        await state.set_state(AdminDelete.serial_kino)

@router.message(AdminDelete.serial_kino)
async def admin_delete_serial_kino(message: Message, state: FSMContext):
    if message.text == "Serial":
        await message.answer("Serial idsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminDeleteSerial.serial_name)
    elif message.text == "Kino":
        await message.answer("Kino idsini kiriting",reply_markup=orqaga)
        await state.set_state(AdminDeleteKino.kino_id)
    elif message.text == "Serial qismi":
        await message.answer("Serial qismini idsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminDeleteSerialQism.serial_qism_id)
    elif message.text == "🔙 orqaga":
        await state.set_state(AdminState.add_remove)
        await message.answer("Tanlang", reply_markup=admin_keyboard)
