from queue import Queue

import telegram
from django.conf import settings
from telegram.ext import Dispatcher

from rw_got.apps.telegram.models import User, Chat, IncomingMessage, \
    OutgoingMessage
from rw_got.apps.telegram.incoming_messages_handlers import handle_message


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
        webhook_url = 'https://{domain}/{path}'.format(
            domain=settings.DOMAIN, path=settings.TELEGRAM_BOT_WEBHOOK_PATH)
        self._bot.setWebhook(webhook_url)
        self._dispatcher = Dispatcher(self._bot, Queue())

    @staticmethod
    def _save_message(update):
        message = update.effective_message
        user = message.from_user
        saved_user, _ = User.objects.get_or_create(
            external_id=user.id,
            defaults={'first_name': user.first_name,
                      'last_name': user.last_name,
                      'username': user.username,
                      'is_bot': user.is_bot,
                      'language_code': user.language_code}

        )
        chat = message.chat
        saved_chat, _ = Chat.objects.get_or_create(
            external_id=chat.id,
            defaults={
                'first_name': chat.first_name,
                'last_name': chat.last_name,
                'username': chat.username,
                'title': chat.title,
                'type': chat.type}
        )
        message, _ = IncomingMessage.objects.get_or_create(
            external_id=message.message_id,
            text=message.text,
            user=saved_user,
            chat=saved_chat,
            defaults={'creation_date': message.date}
        )
        handle_message(message)

    def accept_message(self, update: str):
        update = telegram.Update.de_json(update, self._bot)
        self._save_message(update)
        self._dispatcher.process_update(update)

    def send_message(self, message: OutgoingMessage):
        params = {'chat_id': message.chat.external_id}
        if message.reply_to:
            params['reply_to_message_id'] = message.reply_to.external_id
        if message.text:
            self._bot.send_message(text=message.text, **params)
        if message.photo_url:
            self._bot.send_photo(photo=message.photo_url, **params)
