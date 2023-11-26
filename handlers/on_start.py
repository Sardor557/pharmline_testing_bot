from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from handlers.main_menu import on_main_menu
from loader import dp
from keyboards.default_keyboards.reply_keyboards import select_lang_btn
from states import Conditions
from utils.http_request import is_user_registered


@dp.message_handler(CommandStart(), state='*', chat_type=[types.ChatType.PRIVATE])
async def start(message: types.Message, state):
    chat_id = message.from_user.id

    is_reg = is_user_registered(chat_id)
    print(is_reg)
    if is_reg:
        return await on_main_menu(message, state)

    await message.answer('Выберите язык,\n'
                         'Tilni tanlang,\n'
                         'Choose language', reply_markup=await select_lang_btn())
    await Conditions.choose_lang.set()


