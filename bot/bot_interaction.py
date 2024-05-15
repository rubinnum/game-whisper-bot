from typing import Final
import telebot
from telebot import types
import telegram
import asyncio
from bs4 import BeautifulSoup



bot = telebot.TeleBot('7144215394:AAGJXRA-PYsuczsq-AiPmLuxVBKkdM27lIw', parse_mode=None)
BOT_USERNAME: Final = '@game_whisper_bot'


@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    bot.reply_to(message, ' Welcome to Gaming Whisper')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('Game Profile')
    button_2 = types.InlineKeyboardButton('Personal Recommendation')
    markup.add(button_1, button_2)
    bot.send_message(message.chat.id, "Your choice for today:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

