from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Database.user_serial import get_serial_all, get_serial_fasl
from Keyboards.select_serials_kb import get_serials_keyboard
from Keyboards.serial_fasl import get_serial_fasl_kb
from Keyboards.serial_qismlar import get_qismlar_keyboard
from Keyboards.user_kino_serial import user_choose_kb
from States.user_read_serial import UserSerialState
from Utils.captions import generate_caption


router = Router()

@router.message(F.text == '🎬 Seriallar')
async def user_choose_serials(message: Message, state: FSMContext):
    await message.answer("Qaysi serialni ko'rmoqchisiz?", reply_markup=get_serials_keyboard())
    await state.set_state(UserSerialState.choose_serial)

@router.message(UserSerialState.choose_serial)
async def user_choose_serial(message: Message, state: FSMContext):
    serial_name = message.text
    if serial_name == "🔙 Orqaga":
        await message.answer("Asosiy menyu :", reply_markup=user_choose_kb)
        return
    fasllar = get_serial_fasl(serial_name)
    if fasllar:
        await state.update_data(serial_name=serial_name)
        await message.answer("Qaysi faslni tanlaysiz?", reply_markup=get_serial_fasl_kb(serial_name))
        await state.set_state(UserSerialState.choose_fasl)
    else:
        await message.answer("Bunday serial topilmadi!")

@router.message(UserSerialState.choose_fasl)
async def user_choose_fasl(message: Message, state: FSMContext):
    if message.text == "🔙 Orqaga":
        await message.answer("Qaysi serialni ko'rmoqchisiz?", reply_markup=get_serials_keyboard())
        await state.set_state(UserSerialState.choose_serial)
        return

    # Yangi formatlash: matndan oxirgi 2ta so‘zni ajratib olish
    try:
        parts = message.text.rsplit(" ", 2)  # masalan: ["Qashqirlar makoni", "2", "fasl"]
        serial_name = parts[0]
        fasl = int(parts[1])  # bu endi to‘g‘ri integer bo‘ladi

        await state.update_data(serial_fasl=fasl, serial_name=serial_name)
        seriyalar = get_serial_all(serial_name, fasl)

        if seriyalar:
            qismlar_soni = len(seriyalar)
            await message.answer("Qaysi qismlarni ko'rmoqchisiz?", reply_markup=get_qismlar_keyboard(qismlar_soni, serial_name, fasl))
            await state.set_state(UserSerialState.choose_qismlar)
        else:
            await message.answer("Bu fasl uchun qismlar topilmadi.")
    except Exception as e:
        print(e)
        await message.answer("❌ Xatolik: Fasl va serial nomini aniqlab bo‘lmadi.")



@router.message(UserSerialState.choose_qismlar)
async def user_choose_range(message: Message, state: FSMContext):
    if message.text == "🔙 Orqaga":
        data = await state.get_data()
        await message.answer("Qaysi faslni tanlaysiz?", reply_markup=get_serial_fasl_kb(data["serial_name"]))
        await state.set_state(UserSerialState.choose_fasl)
        return

    data = await state.get_data()
    serial_name = data["serial_name"]
    serial_fasl = data["serial_fasl"]

    try:
        range_text = message.text.strip().split()[0]  # "1-10"
        start, end = map(int, range_text.split("-"))
        all_episodes = get_serial_all(serial_name, serial_fasl)

        selected_eps = all_episodes[start - 1:end]

        for seria in selected_eps:
            caption = generate_caption(seria)
            await message.answer_video(video=seria[8], caption=caption)

    except Exception as e:
        print(f"❌ Xatolik: {e}")
        await message.answer(f"❌ Qismlar oralig'ini aniqlab bo'lmadi.\n{e}")

