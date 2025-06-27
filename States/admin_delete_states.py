from aiogram.fsm.state import StatesGroup, State

class AdminDelete(StatesGroup):
    serial_kino = State()

class AdminDeleteSerial(StatesGroup):
    serial_name = State()

class AdminDeleteSerialQism(StatesGroup):
    serial_qism_id = State()

class AdminDeleteKino(StatesGroup):
    kino_id = State()