from typing import List

from aiogram import types

from filters.call_back_filters import question_filter
from models.ViOption import ViOption
from data.config import _


def variants_btn(options: List[ViOption], lg, choose_option: dict = None):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    if options is not None:
        for option in options:
            title = option.variant
            if choose_option is not None and choose_option.get(option.variant):
                title = f'🟢 {option.variant}'

            variant = types.InlineKeyboardButton(text=title, callback_data=question_filter.new(
                action='variant',
                variant=option.variant,
                optionId=option.id,
                questionId=option.questionId
            ))
            keyboard.insert(variant)

    next = types.InlineKeyboardButton(text=_('Далее', locale=lg), callback_data=question_filter.new(
        action='next',
        variant='none',
        optionId=0,
        questionId=choose_option['questionId'] if choose_option is not None else 0
    ))
    keyboard.add(next)
    return keyboard
