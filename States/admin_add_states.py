from aiogram.fsm.state import State, StatesGroup

class AdminState(StatesGroup):
    add_remove = State()

class AdminCreateSerialState(StatesGroup):
    serial_id = State()
    serial_name = State()
    serial_language = State()
    serial_janr = State()
    serial_year = State()

class AdminSerialAdd(StatesGroup):
    serial = State()
    qism_id = State()
    fasl = State()
    qism = State()
    video = State()

class AdminKinoAdd(StatesGroup):
    kino_id = State()
    kino_name = State()
    kino_language = State()
    kino_year = State()
    kino_janr = State()
    kino_qism = State()
    vide_id = State()
