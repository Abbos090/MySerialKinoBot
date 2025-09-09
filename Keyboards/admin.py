from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Foydalanuvchi")],
        [KeyboardButton(text="Admin")]
    ],
    resize_keyboard=True
)