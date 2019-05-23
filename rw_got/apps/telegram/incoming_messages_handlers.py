from rw_got.apps.telegram.models import OutgoingMessage


def handle_message(message):
    OutgoingMessage.objects.create(chat=message.chat,
                                   reply_to=message,
                                   text="Ходор!")
