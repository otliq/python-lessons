"""
CYRILL LATIN STRING TRANSLITERATOR
sources:
https://github.com/kodchi/uzbek-transliterator
https://github.com/eternnoir/pyTelegramBotAPI
https://python.sariq.dev/
"""

import telebot
from transliterate import to_latin,to_cyrillic

TOKEN = "6187871845:AAHYJBdee3Ap8GRq_5JxQn48JhQ6V803TNk"
bot = telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalam alaykum"
    answer+= "\nEnter a string:"
    bot.reply_to(message, answer)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg)if msg.isascii() else to_latin(msg)
    bot.reply_to(message,answer(msg))

bot.polling()