from aiogram.fsm.state import StatesGroup, State

class UserSerialState(StatesGroup):
    choose_serial = State()
    choose_fasl = State()
    choose_qismlar = State()
