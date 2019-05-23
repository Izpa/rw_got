from django.apps import AppConfig
from django.conf import settings
from telegram.error import RetryAfter
import logging


logger = logging.getLogger(__name__)


class TelegramConfig(AppConfig):
    name = 'rw_got.apps.telegram'

    def ready(self):
        if settings.TELEGRAM_BOT_TOKEN:
            from rw_got.apps.telegram.bot import Bot
            try:
                Bot()
            except RetryAfter:
                logger.warning('Telegram bot retry after error!')

