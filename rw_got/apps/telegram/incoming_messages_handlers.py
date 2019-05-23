from rw_got.apps.telegram.models import OutgoingMessage
import random


def default_trigger(_):
    return True


def words_in_message_trigger(words: [str]):
    def f(m):
        result = False
        if m.text:
            result = any((w.lower() in m.lower() for w in words))
        return result
    return f


def chance_trigger(chance: float):
    return lambda: random.random() <= chance


def reply_text_reaction(t: str):
    return lambda m: OutgoingMessage.objects.create(chat=m.chat,
                                                    reply_to=m,
                                                    text=t)


handlers = [
    [[words_in_message_trigger(['ходор'])], [reply_text_reaction('Ходор!')]],
    [[chance_trigger(0.5)], [reply_text_reaction('Ходор!')]],
]


def handle_message(message):
    for triggers, reactions in handlers:
        if all(t(message) for t in triggers):
            for reaction in reactions:
                reaction(message)
            break
