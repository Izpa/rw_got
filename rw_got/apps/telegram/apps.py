from django.apps import AppConfig
from django.conf import settings


class TelegramConfig(AppConfig):
    name = 'rw_got.apps.telegram'

    def ready(self):
        if settings.TELEGRAM_BOT_TOKEN:
            from rw_got.apps.telegram.bot import Bot
            Bot().register_webhook()
