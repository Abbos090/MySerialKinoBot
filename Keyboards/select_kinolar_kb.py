from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from math import ceil

# HAR BIR SAHIFADA NECHTA ELEMENT BO'LADI (2 ustun bo'lgani uchun juft son bo'lishi tavsiya etiladi)
ITEMS_PER_PAGE = 10

def generate_paginated_keyboard(items: list[str], page: int = 0) -> ReplyKeyboardMarkup:
    total_pages = ceil(len(items) / ITEMS_PER_PAGE)

    # Sahifadagi elementlar
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    current_items = items[start:end]

    # Har bir 2 ta elementdan 1 ta qator qilish
    keyboard_buttons = []
    for i in range(0, len(current_items), 2):
        row = []
        row.append(KeyboardButton(text=current_items[i]))
        if i + 1 < len(current_items):
            row.append(KeyboardButton(text=current_items[i + 1]))
        keyboard_buttons.append(row)

    # Navigatsiya tugmalari
    nav_buttons = []
    if page > 0:
        nav_buttons.append(KeyboardButton(text="⬅️ Oldingi"))
    if page < total_pages - 1:
        nav_buttons.append(KeyboardButton(text="➡️ Keyingi"))

    if nav_buttons:
        keyboard_buttons.append(nav_buttons)

    # Har doim oxirida "🔙 orqaga" tugmasi
    keyboard_buttons.append([KeyboardButton(text="🔙 orqaga")])

    return ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True
    )
