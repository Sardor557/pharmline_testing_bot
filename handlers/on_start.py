from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from utils.on_action import main_menu_action
from loader import dp
from keyboards.default_keyboards.reply_keyboards import select_lang_btn
from states import Conditions
from utils.http_request import is_user_registered_async


@dp.message_handler(CommandStart(), state='*', chat_type=[types.ChatType.PRIVATE])
async def start(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id

    is_reg = await is_user_registered_async(chat_id)
    print(is_reg)
    if is_reg:
        data = await state.get_data()
        return await main_menu_action(chat_id, data['lg'])

    await message.answer('Выберите язык,\n'
                         'Tilni tanlang,\n'
                         'Choose language', reply_markup=select_lang_btn())
    await Conditions.choose_lang.set()


