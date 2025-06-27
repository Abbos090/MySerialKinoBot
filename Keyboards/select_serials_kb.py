from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from Database.select_serials_db import select_serials

def get_serials_keyboard():
    serial_list = list(select_serials()) or []

    keyboard = []
    row = []

    for i, serial in enumerate(serial_list, start=1):
        row.append(KeyboardButton(text=serial[0]))
        if i % 2 == 0:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append([KeyboardButton(text="🔙 Orqaga")])

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)