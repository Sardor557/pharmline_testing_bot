from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import Conditions
from data.config import _
from utils.http_request import get_drugs_async
from keyboards.default_keyboards.reply_keyboards import drugs_btn


@dp.message_handler(state=Conditions.main_menu_state)
async def on_main_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()

    msg = message.text

    if msg == _('📋 Список вопросов'):
        drugs = await get_drugs_async(data['token'])
        await message.answer(_("Выберите препарат по которому вы хотите пройти тестирование"), reply_markup=drugs_btn(drugs.data, data['lg']))
        await Conditions.questions.set()
