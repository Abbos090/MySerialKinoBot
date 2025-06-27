from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_choose_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🎬 Kinolar'), KeyboardButton(text='🎬 Seriallar')],
    ],
    resize_keyboard=True
)