from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from math import ceil

from Database.read_kino import read_kino_db, read_kino_name_db
from Database.select_kinolar import select_kinolar_db
from Keyboards.select_kinolar_kb import generate_paginated_keyboard
from Keyboards.select_kinolar_kb import ITEMS_PER_PAGE
from Keyboards.user_kino_serial import user_choose_kb
from States.user_read_kino import UserReadKinoState


router = Router()

@router.message(F.text.isdigit())
async def kino_user_handler(message: Message):
    id = message.text
    data = read_kino_db(id)
    if data:
        try:
            id = data['id']
            name = data['name']
            language = data['language']
            year = data['year']
            janr = data['janr']
            qism = data['qism']
            sec = data['second']
            video_id = data['video_id']

            hour = sec // 3600
            sec %= 3600
            minute = sec // 60
            sec %= 60
            if hour > 0:
                captions = (
                    f"🎬 {name}\n"
                    f"qism - {qism}\n"
                    f"📆 {year}\n"
                    f"🕜 {hour} soat, {minute} daqiqa, {sec} soniya\n"
                    f"💎 {janr}\n"
                    f"👅 {language}\n"
                )
            else:
                captions = (
                    f"🎬 {name}\n"
                    f"qism - {qism}\n"
                    f"📆 {year}\n"
                    f"🕜 {minute} daqiqa, {sec} soniya\n"
                    f"💎 {janr}\n"
                    f"👅 {language}\n"
                )
            await message.answer_video(video=video_id, caption=captions)

        except Exception as e:
            await message.answer(f"Xatolik yuz berdi {e}")

    else:
        await message.answer("Bunday ID topilmadi.")


@router.message(F.text == "🎬 Kinolar")
async def show_kinolar(message: Message, state: FSMContext):
    items = select_kinolar_db()  # ['Avatar', 'Inception', ...]
    await state.update_data(kinolar=items, kino_page=0)
    keyboard = generate_paginated_keyboard(items, page=0)
    await message.answer("Quyidagilardan birini tanlang:", reply_markup=keyboard)
    await state.set_state(UserReadKinoState.name)

@router.message(UserReadKinoState.name)
async def read_kino_from_db(message: Message, state: FSMContext):
    name = message.text
    if name == '🔙 orqaga':
        await state.clear()
        await message.answer("Asosiy menyu", reply_markup=user_choose_kb)  # yoki oddiy keyboard
        return

    data = read_kino_name_db(name)
    if data:
        try:
            id = data['id']
            name = data['name']
            language = data['language']
            year = data['year']
            janr = data['janr']
            qism = data['qism']
            sec = data['second']
            video_id = data['video_id']

            hour = sec // 3600
            sec %= 3600
            minute = sec // 60
            sec %= 60
            if hour > 0:
                captions = (
                    f"kino id - {id}\n"
                    f"🎬 {name}\n"
                    f"qism - {qism}\n"
                    f"📆 {year}\n"
                    f"🕜 {hour} soat, {minute} daqiqa, {sec} soniya\n"
                    f"💎 {janr}\n"
                    f"🌐 {language}\n\n"
                    f"@seriallar_kinolar_olami bot haqida ma'lumot va muhokama uchun"
                )
            else:
                captions = (
                    f"kino id - {id}\n"
                    f"🎬 {name}\n"
                    f"🎞 {qism}\n"
                    f"📆 {year}\n"
                    f"🕜 {minute} daqiqa, {sec} soniya\n"
                    f"💎 {janr}\n"
                    f"🌐 {language}\n\n"
                    f"@seriallar_kinolar_olami bot haqida ma'lumot va muhokama uchun"
                )
            await message.answer_video(video=video_id, caption=captions)

        except Exception as e:
            await message.answer(f"Xatolik yuz berdi {e}")

    else:
        await message.answer("Bunday Kino topilmadi.")


@router.message(F.text.in_(["⬅️ Oldingi", "➡️ Keyingi"]))
async def handle_navigation(message: Message, state: FSMContext):
    data = await state.get_data()
    items = data.get("kinolar", [])
    page = data.get("kino_page", 0)

    if message.text == "➡️ Keyingi":
        page += 1
    elif message.text == "⬅️ Oldingi":
        page -= 1

    page = max(0, min(page, ceil(len(items) / ITEMS_PER_PAGE) - 1))  # Chegaralarni tekshiramiz

    await state.update_data(kino_page=page)
    keyboard = generate_paginated_keyboard(items, page)
    await message.answer("Quyidagilardan birini tanlang:", reply_markup=keyboard)


@router.message(F.text == "🔙 orqaga")
async def back_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Asosiy menyu", reply_markup=user_choose_kb)  # yoki oddiy keyboard
