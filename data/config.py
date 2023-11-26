import os

from pathlib import Path

from aiogram.contrib.middlewares.i18n import I18nMiddleware

from dotenv import load_dotenv


load_dotenv()

PAYME_TOKEN = os.getenv('PAYME_TOKEN')
CLICK_TOKEN = os.getenv('CLICK_TOKEN')
geocod_api = os.getenv('geocod_api')
BOT_TOKEN = os.getenv('BOT_TOKEN')

I18N_DOMAIN = 'oblacko'
BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'

i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
_ = i18n.gettext


WEBHOOK_HOST = os.getenv('ip')
WEBHOOK_PORT = '8080'
WEBHOOK_PATH = f'/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = '3001'

WEBHOOK_SSL_CERT = '/home/ubuntu/tokiobae_bot/webhook_cert.pem'
# SSL_CERTIFICATE = open(WEBHOOK_SSL_CERT, 'rb').read()
