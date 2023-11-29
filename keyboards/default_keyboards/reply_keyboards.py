from typing import List

from aiogram import types

from data.config import _
from models.ViDrug import ViDrug


def back_button(lg):
    return types.KeyboardButton(_('⬅Назад', locale=lg))


def lang_only_btn():
    russian = types.KeyboardButton('Русский🇷🇺')
    uzbek = types.KeyboardButton("O'zbek🇺🇿")
    english = types.KeyboardButton("English🏴󠁧󠁢󠁥󠁮󠁧󠁿")

    return russian, uzbek, english


def select_lang_btn():
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    langs = [lang['text'] for lang in lang_only_btn()]
    return keyboards.add(*langs)


def change_lang_btn(lg):
    langs = [lang['text'] for lang in lang_only_btn()]
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    return keyboards.add(*langs, back_button(lg))


def request_contact_btn(lg):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    contact = types.KeyboardButton(_('Отправить номер📱', locale=lg), request_contact=True)
    keyboard.add(contact)
    return keyboard


def settings_btn(lg):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    change_lang = types.KeyboardButton(_('🇷🇺Изменить язык', locale=lg))

    keyboard.add(change_lang, back_button(lg))
    return keyboard


def main_menu_btn(lg):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    questions = types.KeyboardButton(_("📋 Список вопросов", locale=lg))
    settings = types.KeyboardButton(_("🛠 Настройки", locale=lg))
    return keyboard.add(questions, settings)


def drugs_btn(drugs: List[ViDrug], lg):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[drug.name for drug in drugs])
    keyboard.add(back_button(lg))
    return keyboard
