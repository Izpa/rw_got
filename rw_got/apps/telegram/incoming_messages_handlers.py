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


default_replies = [{'text': 'Ходор!'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор?'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://cdn.igromania.ru/mnt/news/1/c/2/9/c/9/60784/38d123b411597ba1_848x477.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://lamcdn.net/wonderzine.com/post_image-image/fLPkmDenUkD9wres6U8NAg-article.gif'},
                   {'text': 'Ходор'},
                   {'text': 'Хоходор'},
                   {'photo_url': 'http://images4.wikia.nocookie.net/__cb20120701222239/gameofthrones/images/c/c1/Hodor_infobox.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://cs4.pikabu.ru/post_img/2016/05/23/7/1464002589134327393.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Хдр'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ5bhPrJIPFzetfn6xnE4MVRxrgy2uU-iAWsuId8zzX74GoPV-tQ'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-DxTm2M1Vv2KBybLCgqlm_X7zKWSBALA1Czi3hPp6UJ-tF9ae'},
                   {'text': 'Х-ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://wiki.godville.net/images/thumb/c/cc/%D0%A5%D0%BE%D0%B4%D0%BE%D1%80_%D0%BB%D0%BE%D0%B3%D0%BE.png/250px-%D0%A5%D0%BE%D0%B4%D0%BE%D1%80_%D0%BB%D0%BE%D0%B3%D0%BE.png'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор! Ходор, ходор ходор. Ходор ходор. Ходор - ходор ходор. Ходор? Ходор!'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Hodor!'},
                   {'text': 'Ходор!'},
                   {'photo_url': 'http://www.vladtime.ru/uploads/posts/2016-10/1476281875_kinopoisk.ru-kristian-nairn-2350694.jpg'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3ACjjanlagSdYrJKOcaVTqp38uLf0zsWslIV1T5PCNo4WG8tdRw'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'text': 'Ходорррррррррр'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://www.vokrug.tv/pic/person/4/e/0/f/4e0f3d117d07f831bd05b9cffa59dd0e.jpeg'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://pregel.info/wp-content/uploads/2018/12/Hodor-London.jpg'},
                   {'text': 'Ходооор'},
                   {'photo_url': 'https://i.ebayimg.com/images/g/n2EAAOSwRXJceh77/s-l300.jpg'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://24smi.org/public/media/resize/660x-/person/2018/03/14/mprp6k2zfkx9-khodor.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Хоооооодор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIewSpoBxOBhZHKJA8goGHPwtlzPKbYKD2P13w2REKZ34vryS8'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://shop.eaglemoss.com/ru/images/shop_products/8c59418e-5871-4373-acfb-7617164d6204.jpg'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://24smi.org/public/media/resize/800x-/2018/3/14/zh_3FjmOK0.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор-ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://www.gametech.ru/sadm_images/2008/2016_ap/Virginia/Clipboard03.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор...'},
                   {'photo_url': 'https://cs5.pikabu.ru/post_img/big/2015/06/10/10/1433958921_519000784.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://www.parazitakusok.ru/images/item/1789/MOD.jpg'},
                   {'text': 'Ходор'},
                   {'text': 'Хдр'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://qph.fs.quoracdn.net/main-qimg-d9d48b4d1cbca3a5bb845b2b1d20cffb.webp'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh9XataWJ6Wu7Y78Sh9rZON1WqcuYT8OhE4N14CgBqwwHFVweB5Q'},
                   {'text': 'Ходор'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://imagesvc.timeincapp.com/v3/fan/image?url=https%3A%2F%2Fwinteriscoming.net%2Ffiles%2F2017%2F04%2FScreen-Shot-2017-04-07-at-10.19.52-AM-2.jpg&c=sc&w=736&h=485'},
                   {'text': 'Ходор'},
                   {'text': 'ХОДОР ХОДОР ХОДОР ХОДОР ХОДОР ХОДОР ХОДОР ХОДОР'},
                   {'text': 'Ходор'},
                   {'photo_url': 'https://pbs.twimg.com/profile_images/378800000045906785/debb0a39ea1a3bb337a18f9d17a8b8c8_400x400.jpeg'},
                   {'text': 'Ходор'},
                   ]
default_replies_reaction = reply_cycle_reaction(default_replies,
                                                'DEFAULT_REPLIES_INDEX')

door_replies = [{'photo_url': 'https://memepedia.ru/wp-content/uploads/2017/09/7DB.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://img.tsn.ua/cached/1533894782/tsn-0836864a16c9e8e7a60a1868506671d8/thumbs/1340x530/d4/10/9e51cd099d6e3f54cbf8abfadee310d4.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn9GQ6Hfm7yaH-FcZh4Ghv9axz8MRFZbcqMLx0W2-grr7Gr-OSSw'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://img.joinfo.ua/i/2018/06/5b2ceaedc9125.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://cs4.pikabu.ru/post_img/2016/05/26/7/1464259400193537880.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://memepedia.ru/wp-content/uploads/2017/09/https-2F2Fblueprint-api-production.s3.amazonaws.com2Fuploads2Fcard2Fimage2F960932FHodor_Sticker_elevator.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://zoko.com.ua/sites/default/files/poster/cpp20246.jpg'},
                   {'text': 'Ходор'},
                {'photo_url': 'https://images-na.ssl-images-amazon.com/images/I/715lTR9YCGL._SX466_.jpg'},
                   {'text': 'Ходор'},
                ]
door_replies_reaction = reply_cycle_reaction(door_replies,
                                             'DOOR_REPLIES_INDEX')

handlers = [
    # Disable bot
    [[bot_is_enable_trigger(),
      is_creator_trigger(),
      phrases_in_message_trigger(['остановить моторику',
                                  'усни глубоким сном без сновидений'])],
     [disable_bot_reaction()]],

    [[bot_is_enable_trigger(),
      phrases_in_message_trigger(['дверь', 'door', 'hold', 'gate', 'close', 'закрой', 'держи', 'ход', 'затвор'])],
     [door_replies_reaction]],

    [[bot_is_enable_trigger(),
      phrases_in_message_trigger(['ходор', 'hodor', 'ходо', 'одор'])],
     [default_replies_reaction]],

    [[bot_is_enable_trigger(),
      chance_trigger(0.05)],
     [default_replies_reaction]],
]


def handle_message(message):
    for triggers, reactions in handlers:
        if all(t(message) for t in triggers):
            for reaction in reactions:
                reaction(message)
            break
