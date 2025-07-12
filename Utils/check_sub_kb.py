from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_subs_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Obuna bo‘ldim", callback_data="check_subs")]
    ])
