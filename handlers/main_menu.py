from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import Conditions
from utils.on_action import main_menu_action


@dp.message_handler(state=Conditions.main_menu_state)
async def on_main_menu(message: types.Message, state: FSMContext):
    lg = await state.get_data()
    lg = lg['lg']
    return await main_menu_action(message.from_user.id, lg)
