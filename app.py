# from data.config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, SSL_CERTIFICATE
from loader import bot

from handlers import dp


async def main(dp):
    # await bot.set_webhook(
    #     url=WEBHOOK_URL,
    #     certificate=SSL_CERTIFICATE
    # )
    pass


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from aiogram.utils import executor
    executor.start_polling(dp, skip_updates=True, on_startup=main, on_shutdown=on_shutdown)
    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=main,
    #     on_shutdown=on_shutdown,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT,
    # )
