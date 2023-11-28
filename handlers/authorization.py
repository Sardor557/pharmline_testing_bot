from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from models.AuthorizationModel import AuthorizationModel
from states import Conditions
from utils.http_request import authorize_async
from utils.on_action import password_action, main_menu_action


@dp.message_handler(state=Conditions.request_contact, content_types=['contact'])
async def get_contact(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    chat_id = message.from_user.id

    lg = await state.get_data()
    lg = lg['lg']

    await state.update_data({"phone": phone})
    return await password_action(chat_id, lg)


@dp.message_handler(state=Conditions.request_password)
async def get_password(message: types.Message, state: FSMContext):
    password = message.text
    chat_id = message.from_user.id

    data = await state.get_data()
    model = AuthorizationModel(
        phone=data['phone'],
        password=password,
        telegramId=chat_id,
        lang=data['lg']
    )

    res = await authorize_async(model)
    if not res.isSuccess:
        return await message.answer(res.message)

    update = {
        'id': res.data.id,
        'telegramId': res.data.telegramId,
        'token': res.data.token,
    }
    await state.update_data(update)
    await main_menu_action(chat_id, data['lg'])
    await Conditions.main_menu_state.set()
