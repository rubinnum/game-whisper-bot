import telebot
from telebot import types

from constants import BOT_TOKEN
from get_game_info import output_game_data
from get_recommendations_list import output_recommended_games

bot = telebot.TeleBot(BOT_TOKEN)

user_states = {}
STATE_WAIT_FOR_GAME_NAME = "waiting for game name to be profiled"
STATE_WAIT_FOR_RECOMMENDATION = "waiting for recommendation"

@bot.message_handler(commands=['hi', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to Gaming Whisper')
    markup = types.InlineKeyboardMarkup(row_width=2)
    game_profile_button = types.InlineKeyboardButton('Game Profile', callback_data='game_profile')
    recommendation_button = types.InlineKeyboardButton('Personal Recommendation', callback_data='recommendation')
    markup.add(game_profile_button, recommendation_button)
    bot.send_message(message.chat.id, "Your choice for today:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'game_profile':
        bot.send_message(call.message.chat.id, "Enter name of the game")
        user_states[call.message.chat.id] = STATE_WAIT_FOR_GAME_NAME
    elif call.data == 'recommendation':
        bot.send_message(call.message.chat.id, "List your games for recommendations")
        user_states[call.message.chat.id] = STATE_WAIT_FOR_RECOMMENDATION

@bot.message_handler(func=lambda message: message.chat.id in user_states)
def handle_message(message):
    state = user_states.get(message.chat.id)

    if state == STATE_WAIT_FOR_GAME_NAME:
        bot.reply_to(message, f"Fetching game Profile: {message.text}")
        game_info = output_game_data(message.text)
        if game_info:
            bot.send_message(message.chat.id, game_info)
        else:
            bot.send_message(message.chat.id, f"No information found for '{message.text}'")
        del user_states[message.chat.id]

    elif state == STATE_WAIT_FOR_RECOMMENDATION:
        bot.reply_to(message, f"Fetching list: {message.text}")
        recommendations = output_recommended_games(message.text)
        if recommendations:
            bot.send_message(message.chat.id, recommendations)
        else:
            bot.send_message(message.chat.id, f"No recommendations found for '{message.text}'")
        del user_states[message.chat.id]


if __name__ == '__main__':
    bot.infinity_polling()
