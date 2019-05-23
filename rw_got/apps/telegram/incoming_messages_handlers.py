from rw_got.apps.telegram.models import OutgoingMessage


def any_message_trigger(_):
    return True


def hodor_reaction(message):
    OutgoingMessage.objects.create(chat=message.chat,
                                   reply_to=message,
                                   text="Ходор!")


handlers = ((any_message_trigger, hodor_reaction),
            )


def handle_message(message):
    for trigger, reaction in handlers:
        if trigger(message):
            reaction(message)
            break
