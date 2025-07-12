from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_subs_keyboard(channels: list[str]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=f"➕ {channel}", url=f"https://t.me/{channel[1:]}")]
        for channel in channels
    ]
    buttons.append([
        InlineKeyboardButton(text="✅ Obuna bo‘ldim", callback_data="check_subs")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
