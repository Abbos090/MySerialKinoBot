from aiogram import Bot
from aiogram.types import ChatMember
from aiogram.exceptions import TelegramBadRequest

# 🛠️ Obuna bo‘lishi kerak bo‘lgan kanallar
REQUIRED_CHANNELS = ['@seriallar_kinolar_olami']  # <-- O'zingizning kanallaringizni yozing

async def check_user_subscriptions(bot: Bot, user_id: int) -> list[str]:
    """Foydalanuvchining barcha kerakli kanallarga obuna bo'lganligini tekshiradi"""
    not_subscribed = []
    for channel in REQUIRED_CHANNELS:
        try:
            member: ChatMember = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ("member", "administrator", "creator"):
                not_subscribed.append(channel)
        except TelegramBadRequest:
            not_subscribed.append(channel)
    return not_subscribed
