import logging
import unittest

from get_game_info import get_game_data


class TestParsing(unittest.TestCase):

    def test_parsing_valid_game(self):
        game_name = 'Skyrim'
        logging.info(f'The game name is {game_name}')

        logging.info('The data is about to be parsed...')
        game_data = get_game_data(game_name)

        self.assertIsNotNone(game_data, 'The data was not parsed successfully')


if __name__ == '__main__':
    unittest.main()
