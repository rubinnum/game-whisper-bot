from typing import Final

import telebot
from telebot import types

from constants import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['hi', 'start'])
def send_welcome(message):
    bot.reply_to(message, ' Welcome to Gaming Whisper')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    game_profile_button = types.InlineKeyboardButton('Game Profile')
    recommendation_button = types.InlineKeyboardButton('Personal Recommendation')
    markup.add(game_profile_button, recommendation_button)
    bot.send_message(message.chat.id, "Your choice for today:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
