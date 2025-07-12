from aiogram import Router, Bot, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from config import ADMINS
from States.admin_add_states import AdminState, AdminCreateSerialState, AdminSerialAdd, AdminKinoAdd
from States.admin_delete_states import AdminDelete, AdminDeleteSerial, AdminDeleteKino, AdminDeleteSerialQism
from Keyboards.admin_keyboards import admin_keyboard
from Keyboards.select_serials_kb import get_serials_keyboard
from Keyboards.delete_serial_kino_kb import delete_serial_kino
from Keyboards.orqaga import orqaga
from Keyboards.user_kino_serial import user_choose_kb

from Utils.check_sub_kb import confirm_subs_keyboard
from Utils.check_subs import check_user_subscriptions

router = Router()


# /start komandasi va dastlabki kirish
@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext, bot: Bot):
    not_subscribed = await check_user_subscriptions(bot, message.from_user.id)
    if not_subscribed:
        links = "\n".join(
            [f"👉 <a href='https://t.me/{ch[1:]}'>{ch}</a>" for ch in not_subscribed]
        )
        await message.answer(
            f"Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:\n\n{links}",
            reply_markup=confirm_subs_keyboard(),
            disable_web_page_preview=True
        )
        return

    if message.from_user.id in ADMINS:
        await message.answer("Xush kelibsiz admin!", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
    else:
        await message.answer(f"Xush kelibsiz {message.from_user.full_name}")
        await message.answer("Kino kodini kiriting yoki tanlang :", reply_markup=user_choose_kb)


# Obuna bo‘ldim tugmasi bosilganda tekshiradi
@router.callback_query(F.data == "check_subs")
async def confirm_subs_callback(callback: CallbackQuery, bot: Bot, state: FSMContext):
    not_subscribed = await check_user_subscriptions(bot, callback.from_user.id)
    if not_subscribed:
        links = "\n".join(
            [f"👉 <a href='https://t.me/{ch[1:]}'>{ch}</a>" for ch in not_subscribed]
        )
        await callback.message.edit_text(
            f"⚠️ Hali quyidagi kanallarga obuna bo‘lmagansiz:\n\n{links}",
            reply_markup=confirm_subs_keyboard(),
            disable_web_page_preview=True
        )
    else:
        await callback.message.delete()
        if callback.from_user.id in ADMINS:
            await callback.message.answer("Xush kelibsiz admin!", reply_markup=admin_keyboard)
            await state.set_state(AdminState.add_remove)
        else:
            await callback.message.answer(f"Xush kelibsiz {callback.from_user.full_name}")
            await callback.message.answer("Kino kodini kiriting yoki tanlang :", reply_markup=user_choose_kb)


# Admin menyusi: tanlashlar
@router.message(AdminState.add_remove)
async def admin_add_remove_handler(message: Message, state: FSMContext):
    if message.text == "Serial yaratish":
        await message.answer("Yaratmoqchi bo'lgan serialingizni IDsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminCreateSerialState.serial_id)
    elif message.text == "Serial qo'shish":
        await message.answer("Qaysi serialga qo'shmoqchisiz", reply_markup=get_serials_keyboard())
        await state.set_state(AdminSerialAdd.serial)
    elif message.text == "Kino qo'shish":
        await message.answer("Qo‘shmoqchi bo‘lgan kino IDsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminKinoAdd.kino_id)
    elif message.text == "O'chirish":
        await message.answer("Qaysi kategoriya o‘chiriladi?", reply_markup=delete_serial_kino)
        await state.set_state(AdminDelete.serial_kino)


# Admin: O‘chirish menyusi
@router.message(AdminDelete.serial_kino)
async def admin_delete_serial_kino(message: Message, state: FSMContext):
    if message.text == "Serial":
        await message.answer("Serial IDsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminDeleteSerial.serial_name)
    elif message.text == "Kino":
        await message.answer("Kino IDsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminDeleteKino.kino_id)
    elif message.text == "Serial qismi":
        await message.answer("Serial qism IDsini kiriting", reply_markup=orqaga)
        await state.set_state(AdminDeleteSerialQism.serial_qism_id)
    elif message.text == "🔙 orqaga":
        await message.answer("Tanlang", reply_markup=admin_keyboard)
        await state.set_state(AdminState.add_remove)
