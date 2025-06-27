from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Serial yaratish"), KeyboardButton(text="Kino qo'shish")],
        [KeyboardButton(text="Serial qo'shish"), KeyboardButton(text="O'chirish")]
    ],
    resize_keyboard=True
)