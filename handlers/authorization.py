from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import Conditions
from utils.on_action import password_action


@dp.message_handler(state=Conditions.request_contact)
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    chat_id = message.from_user.id

    lg = await state.get_data()
    lg = lg['lg']

    await state.update_data({"phone": phone})
    return await password_action(chat_id, lg)


@dp.message_handler(state=Conditions.request_password)
async def get_password(message: types.Message, state: FSMContext):


    await Conditions.questions.set()