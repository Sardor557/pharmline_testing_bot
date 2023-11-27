from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import Conditions
from utils.on_action import login_action


@dp.message_handler(state=Conditions.choose_lang)
async def get_language(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    msg = message.text

    if msg == 'Русский🇷🇺':
        lg = 'ru'
    elif msg == "O'zbek🇺🇿":
        lg = 'uz'
    elif msg == 'English🏴󠁧󠁢󠁥󠁮󠁧󠁿':
        lg = 'en'
    else:
        return

    await state.update_data({"lg": lg})
    return await login_action(chat_id, lg)
