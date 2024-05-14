import openai
from constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_recommended_games(favourite_games):
    pass


if __name__ == '__main__':
    preferences = input('What are the games that you like (divide them with newline): ')
    favourite_games = preferences.split('\n')
    favourite_games = [game.strip() for game in favourite_games]
    get_recommended_games(favourite_games)
