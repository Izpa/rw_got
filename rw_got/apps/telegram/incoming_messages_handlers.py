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
    def f(_):
        config.TELEGRAM_BOT_ENABLE = False

    return f


def enable_bot_reaction():
    def f(_): config.TELEGRAM_BOT_ENABLE = True

    return f


def reply_reaction(text: str = None, photo_url: str = None):
    return lambda m: OutgoingMessage.objects.create(chat=m.chat,
                                                    reply_to=m,
                                                    text=text,
                                                    photo_url=photo_url)


def reply_cycle_reaction(replies: [], index_name: str):
    def f(m):
        i = config.__getattr__(index_name)
        i = 0 if i >= len(replies) else i
        OutgoingMessage.objects.create(chat=m.chat,
                                       reply_to=m,
                                       **replies[i])
        config.__setattr__(index_name, i + 1)

    return f


default_replies = [{'text': 'Ходор!', 'photo_url': 'https://cdn.igromania.ru/mnt/news/1/c/2/9/c/9/60784/38d123b411597ba1_848x477.jpg'},
                   {'text': 'Ходор! Ходор, ходор ходор. Ходор ходор. Ходор - ходор ходор. Ходор? Ходор!'},
                   {'text': 'Hodor!'},
                   {'text': 'Ходор!'},
                   {'text': 'Ходорррррррррр', 'photo_url': 'https://www.vokrug.tv/pic/person/4/e/0/f/4e0f3d117d07f831bd05b9cffa59dd0e.jpeg'}]
default_replies_reaction = reply_cycle_reaction(default_replies,
                                                'DEFAULT_REPLIES_INDEX')

handlers = [
    # Disable bot
    [[bot_is_enable_trigger(),
      is_creator_trigger(),
      phrases_in_message_trigger(['остановить моторику',
                                  'усни глубоким сном без сновидений'])],
     [disable_bot_reaction()]],

    [[bot_is_enable_trigger(),
      phrases_in_message_trigger(['ходор'])],
     [reply_reaction(text='Ходор!')]],

    [[bot_is_enable_trigger(),
      chance_trigger(0.05)],
     [reply_reaction(text='Ходор!')]],
]


def handle_message(message):
    for triggers, reactions in handlers:
        if all(t(message) for t in triggers):
            for reaction in reactions:
                reaction(message)
            break
