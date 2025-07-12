from aiogram import Bot
from aiogram.types import ChatMember
from aiogram.exceptions import TelegramBadRequest

# ❗ Faqat kanal USERNAME (t.me/... emas)
REQUIRED_CHANNELS = ['@seriallar_kinolar_olami']  # o'zingizga moslang

async def check_user_subscriptions(bot: Bot, user_id: int) -> list[str]:
    """Foydalanuvchi obuna bo‘lmagan kanallar roʻyxatini qaytaradi"""
    not_subscribed = []
    for channel in REQUIRED_CHANNELS:
        try:
            member: ChatMember = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ("member", "administrator", "creator"):
                not_subscribed.append(channel)
        except TelegramBadRequest:
            not_subscribed.append(channel)
    return not_subscribed
