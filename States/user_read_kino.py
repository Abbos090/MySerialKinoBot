from aiogram.fsm.state import StatesGroup, State

class UserReadKinoState(StatesGroup):
    name = State()