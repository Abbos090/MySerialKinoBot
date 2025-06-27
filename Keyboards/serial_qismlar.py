from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_qismlar_keyboard(qismlar_soni, serial_name, serial_fasl):
    keyboard = []
    row = []
    step = 5  # 5 ta qismdan iborat bo‘lsin
    for start in range(1, qismlar_soni + 1, step):
        end = min(start + step - 1, qismlar_soni)
        text = f"{serial_name} ({serial_fasl}-fasl) {start}-{end} qism"
        row.append(KeyboardButton(text=text))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    keyboard.append([KeyboardButton(text="🔙 Orqaga")])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
