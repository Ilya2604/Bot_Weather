import telebot
import config
from handlers import start_handler, help_handler, info_handler, callback_handler, weather_handler

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'старт'])
def start(message):
    start_handler(bot, message)


@bot.message_handler(commands=['help', 'помощь'])
def help(message):
    help_handler(bot, message)


@bot.message_handler(commands=['info', 'инфо'])
def info(message):
    info_handler(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    callback_handler(bot, call)


@bot.message_handler(func=lambda message: True)
def get_weather(message):
    weather_handler(bot, message)


if __name__ == '__main__':
    bot.polling(non_stop=True)
