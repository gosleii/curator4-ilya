import telebot

tgbot = telebot.TeleBot('1125811332:AAGMQFHCEHV1Lswxr7aodPbgpyhVkQXVP6k')

@tgbot.message_handler(commands=['start'])
def main(message):
    tgbot.send_message(message.chat.id, '*Привет!*\nЯ так рад, что ты попал ко мне!\nЕсли тебе скучно или я тебе нужен, то напиши _/run_)', parse_mode='Markdown')

@tgbot.message_handler(commands=['run'])
def main(message):
    tgbot.send_message(message.chat.id, 'Ого, ты запустил меня! Мне ооочень приятно)\nЯ пока что не мастер во всех этих ваших технологиях, но знаю твоё будущее) В этой жизни всё у тебя будет хорошо!!!\nНо если уж очень хочешь, то могу посоветовать какую музыку послушать. Скорее напиши мне _/link_ и познаешь все прелести музыки!', parse_mode='Markdown')

@tgbot.message_handler(commands=['link'])
def main(message):
    tgbot.send_message(message.chat.id, 'Если хочешь быть плохишом, то послушай-ка их):\n_ALBLAK 52 (https://music.yandex.ru/artist/17303154)_\n_OBLADAET (https://music.yandex.ru/artist/3676308)_\nМожно чуть поспокойнее:\n_FRIENDLY THUG 52 NGG (https://music.yandex.ru/artist/12666124)_\nНу а если ты всегда спокоен "как удав" и тебе нравятся любовные истории, то послушай его:\n_МОТ (https://music.yandex.ru/artist/1636897)_', parse_mode='Markdown')
    tgbot.send_message(message.chat.id, 'Если я тебе хоть чем-то помог, то просто напиши _/thanks_\nЭто мне будет приятнее всего)', parse_mode='Markdown')

@tgbot.message_handler(commands=['thanks'])
def main(message):
    tgbot.send_message(message.chat.id, 'Обращайся, бро)\nВсегда рад тебе помочь!\nНикогда не предам братишку!', parse_mode='Markdown')

tgbot.infinity_polling()