from queue import Queue

import telegram
from django.conf import settings
from telegram.ext import Dispatcher

from rw_got.apps.telegram.models import User, Chat, IncomingMessage, \
    OutgoingMessage


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Bot(metaclass=Singleton):

    def __init__(self):
        self._bot = telegram.Bot(settings.TELEGRAM_BOT_TOKEN)
        self._bot.setWebhook(
            f'https://{settings.DOMAIN}/{settings.TELEGRAM_BOT_WEBHOOK_PATH}')
        self._dispatcher = Dispatcher(self._bot, Queue())

    @staticmethod
    def _save_message(update):
        message = update.effective_message
        user = message.from_user
        saved_user = User.objects.get_or_create(
            external_id=user.id,
            defaults={'first_name': user.first_name,
                      'last_name': user.last_name,
                      'username': user.username,
                      'is_bot': user.is_bot,
                      'language_code': user.language_code}

        )
        chat = message.chat
        saved_chat = Chat.objects.get_or_create(
            external_id=chat.id,
            defaults={
                'first_name': chat.first_name,
                'last_name': chat.last_name,
                'username': chat.username,
                'title': chat.title,
                'type': chat.type,
                'all_members_are_administrators':
                    chat.all_members_are_administrators}
        )
        IncomingMessage.objects.get_or_create(
            external_id=message.message_id,
            text=message.text,
            user=saved_user,
            chat=saved_chat,
            defaults={'creation_date': message.date}
        )

    def accept_message(self, update: str):
        update = telegram.Update.de_json(update, self._bot)
        self._save_message(update)
        self._dispatcher.process_update(update)

    def send_message(self, message: OutgoingMessage):
        self._bot.send_message(chat_id=message.chat.id, text=message.text)