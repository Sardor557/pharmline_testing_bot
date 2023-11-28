from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline_keyboards.inline_buttons import variants_btn
from loader import dp
from models.ViQuestion import ViQuestion
from states import Conditions
from data.config import _
from utils.http_request import get_drug_id_async, get_drug_question_async
from keyboards.default_keyboards.reply_keyboards import drugs_btn
from utils.on_action import main_menu_action


@dp.message_handler(state=Conditions.questions)
async def drug_questions(message: types.Message, state: FSMContext):
    msg = message.text
    data = await state.get_data()
    token = data['token']

    drug_id = await get_drug_id_async(token, msg)
    if drug_id.data == 0:
        return await message.answer(drug_id.message)

    await state.update_data({'drugId': drug_id.data})

    question = await get_drug_question_async(token, drug_id.data, 0)
    question_data: ViQuestion = question.data
    if not question.isSuccess:
        return await message.answer(question.message)

    await message.answer(question.data.context, reply_markup=variants_btn(question_data.options, data['lg']))
    await Conditions.testing.set()
