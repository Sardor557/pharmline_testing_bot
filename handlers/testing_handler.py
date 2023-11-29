from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline_keyboards.inline_buttons import variants_btn
from loader import dp
from models.ViQuestion import ViQuestion
from models.viAnswer import ViAnswer
from states import Conditions
from data.config import _
from utils.http_request import get_drug_question_async, add_answer_async, get_current_question_async
from utils.on_action import main_menu_action
from filters.call_back_filters import question_filter


@dp.message_handler(state=Conditions.testing)
async def on_message(message: types.Message, state: FSMContext):
    msg = message.text
    chat_id = message.from_user.id
    cache = await state.get_data()
    lg = cache['lg']

    if msg == _('⬅Назад', locale=lg):
        return main_menu_action(chat_id, lg)


@dp.callback_query_handler(question_filter.filter(), state=Conditions.testing)
async def choose_answer(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    cache = await state.get_data()
    action = callback_data['action']
    lg = cache['lg']
    token = cache['token']
    question_id = callback_data['questionId']

    if action == 'variant':
        answer = ViAnswer(employeeId=cache['employeeId'],
                          questionId=question_id,
                          optionId=callback_data['optionId'])

        await state.update_data({'currentQuestion': answer.questionId})
        question = await get_current_question_async(token, question_id)
        choose = {
            callback_data['variant']: callback_data['optionId'],
            'questionId': answer.questionId
                  }
        await state.update_data({'answer': answer.__dict__})
        return await call.message.edit_reply_markup(reply_markup=variants_btn(question.data.options, lg, choose))
    cache = await state.get_data()

    if not cache.get('currentQuestion'):
        return await call.answer(_("Выберите вариант ответа", locale=lg), show_alert=True)

    answer: ViAnswer = ViAnswer(**cache['answer'])
    if question_id != answer.questionId:
        return await call.answer(_("Выберите вариант ответа", locale=lg), show_alert=True)

    res = await add_answer_async(token, answer)
    if not res.isSuccess:
        return await call.message.answer(res.message)

    question = await get_drug_question_async(token, cache['drugId'], answer.questionId)
    if not question.isSuccess:
        await call.message.delete()
        await call.message.answer(question.message)
        return await main_menu_action(call.from_user.id, lg)

    question_data: ViQuestion = question.data
    await call.message.delete()
    await call.message.answer(question_data.context, reply_markup=variants_btn(question_data.options, lg))
