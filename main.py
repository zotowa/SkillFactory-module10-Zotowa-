# Имя бота в Telegram - Converter (https://t.me/ConverterNew_bot)
# Токен бота - 5916792830:AAFXPECiYxyaCO8XCuzI9pjY3pXRFEg9rgI

import telebot
from config import *
from extensions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду, в следующем формате(через пробел):\n\n\
- Имя валюты\n- В какую валюту перевести\n- Колличество переводимой валюты\n\n\
Список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def echo_test(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key, value in keys2.items():
        text = '\n'.join((text, (f'{value} - {key}')))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split()

        if len(values) > 3:
            raise APIException('Слишком много параметров.')
        elif len(values) < 3:
            raise APIException('Слишком мало параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} x {quote} = {total_base * float(amount)} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
