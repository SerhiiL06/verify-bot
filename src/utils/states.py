from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    connect_wallet = State()
    main_menu = State()
    chat_id = State()
    message = State()
