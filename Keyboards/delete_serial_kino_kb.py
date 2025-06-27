from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

delete_serial_kino = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Serial"), KeyboardButton(text="Serial qismi")],
        [KeyboardButton(text="Kino"), KeyboardButton(text="🔙 orqaga")]
    ],
    resize_keyboard=True
)