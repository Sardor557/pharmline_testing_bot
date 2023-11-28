from aiogram.dispatcher.filters.state import StatesGroup, State


class Conditions(StatesGroup):
    choose_lang = State()
    request_contact = State()
    request_password = State()
    main_menu_state = State()
    questions = State()
    testing = State()

