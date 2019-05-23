from rw_got.apps.telegram.models import OutgoingMessage
from constance import config
import random


def default_trigger(_):
    return True


def phrases_in_message_trigger(words: [str]):
    def f(m):
        result = False
        if m.text:
            result = any((w.lower() in m.text.lower() for w in words))
        return result
    return f


def is_creator_trigger():
    return lambda m: m.user.external_id == 112789249


def bot_is_enable_trigger():
    return lambda _: config.TELEGRAM_BOT_ENABLE


def bot_is_disable_trigger():
    return lambda _: not config.TELEGRAM_BOT_ENABLE


def chance_trigger(chance: float):
    return lambda _: random.random() <= chance


def disable_bot_reaction():
    def f(_): config.TELEGRAM_BOT_ENABLE = False
    return f


def enable_bot_reaction():
    def f(_): config.TELEGRAM_BOT_ENABLE = True
    return f


def reply_text_reaction(t: str):
    return lambda m: OutgoingMessage.objects.create(chat=m.chat,
                                                    reply_to=m,
                                                    text=t)


handlers = [
    # Disable bot
    [[bot_is_enable_trigger(),
      is_creator_trigger(),
      phrases_in_message_trigger(['остановить моторику',
                                  'усни глубоким сном без сновидений'])],
     [disable_bot_reaction()]],

    [[bot_is_enable_trigger(),
      phrases_in_message_trigger(['ходор'])],
     [reply_text_reaction('Ходор!')]],

    [[bot_is_enable_trigger(),
      chance_trigger(0.05)],
     [reply_text_reaction('Ходор!')]],
]


def handle_message(message):
    for triggers, reactions in handlers:
        if all(t(message) for t in triggers):
            for reaction in reactions:
                reaction(message)
            break
