from telebot import types
from weather_location import get_weather, get_location


def start_handler(bot, message):
    keyboard = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('Кнопка 1', callback_data='Кнопка 1')
    btn_2 = types.InlineKeyboardButton('Кнопка 2', callback_data='Кнопка 2')
    keyboard.row(btn_1, btn_2)
    btn_3 = types.InlineKeyboardButton('Кнопка 3', callback_data='Кнопка 3')
    keyboard.row(btn_3)
    bot.reply_to(message, f"Привет! {message.from_user.first_name} Я бот погоды. Введи название города, чтобы узнать погоду.", reply_markup=keyboard)


def help_handler(bot, message):
    bot.send_message(message.chat.id, 'Чем могу помочь')


def info_handler(bot, message):
    bot.send_message(message.chat.id, 'Какая то информация')


def callback_handler(bot, call):
  if call.data == 'Кнопка 1':
    bot.send_message(call.message.chat.id, 'Кнопка 1')
  elif call.data == 'Кнопка 2':
    bot.send_message(call.message.chat.id, 'Кнопка 2')
  elif call.data == 'Кнопка 3':
      bot.send_message(call.message.chat.id, 'Кнопка 3')


def weather_handler(bot, message):
    city = message.text.strip()

    # Получение координат города
    location = get_location(city)

    if location is not None:
        lat, lon = location
        if lat is not None and lon is not None:
            # Получение данных о погоде
            weather_data = get_weather(lat, lon)

            if weather_data:
                temp = weather_data['main']['temp']
                condition = weather_data['weather'][0]['description']
                bot.reply_to(message, f"Температура в {city}: {temp}°C, Состояние: {condition}")
            else:
                bot.reply_to(message, "Не удалось получить данные о погоде. Попробуйте позже.")
        else:
            bot.reply_to(message,
                         "Не удалось определить координаты города. Проверьте название города и попробуйте снова.")
    else:
        bot.reply_to(message, "Не удалось определить координаты города. Проверьте название города и попробуйте снова.")
