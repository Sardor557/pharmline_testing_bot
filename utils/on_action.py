from aiogram.utils.markdown import hbold
from aiogram import types

from keyboards.default_keyboards.reply_keyboards import main_menu_btn, settings_btn, request_contact_btn
from loader import bot
from data.config import _
from states import Conditions


async def login_action(chat_id, lg):
    send_phone = hbold(_('Отправить номер📱', locale=lg))
    text = _("Пройдите авторизацию. Для начала отправьте свой номер нажав на кнопку ", locale=lg) + send_phone
    await bot.send_message(chat_id, _(text, locale=lg), reply_markup=request_contact_btn(lg))
    await Conditions.request_contact.set()


async def password_action(chat_id, lg):
    text = _("Теперь введите пароль. Если вы не знаете свой пароль, позвоните в офис", locale=lg)
    await Conditions.request_password.set()
    await bot.send_message(chat_id, text, reply_markup=types.ReplyKeyboardRemove())


async def main_menu_action(chat_id, lg):
    await bot.send_message(chat_id, _("Хотите пройти тестирование?", locale=lg), reply_markup=main_menu_btn(lg))
    await Conditions.main_menu_state.set()
