from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from Database.user_serial import get_serial_fasl

def get_serial_fasl_kb(serial_name):
    fasl_list = get_serial_fasl(serial_name)

    keyboard = [[KeyboardButton(text=f'{serial_name} {fasl} fasl')] for fasl in fasl_list]
    keyboard.append([KeyboardButton(text="🔙 Orqaga")])  # 🔙 qo‘shildi

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
