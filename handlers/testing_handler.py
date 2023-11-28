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
from filters.call_back_filters import question_filter


@dp.callback_query_handler(question_filter.filter(), state=Conditions.testing)
async def choose_answer(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    cache = await state.get_data()
    print(callback_data)