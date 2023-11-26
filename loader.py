import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data.config import BOT_TOKEN

#
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
#                         level=logging.ERROR, filename='restoraunbot.log')

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
storage = RedisStorage2()
dp = Dispatcher(bot=bot, storage=storage)
