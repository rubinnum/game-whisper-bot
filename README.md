# Game Whisper Bot

## Overview

This project is developed as part of a Software Engineering class. The Game Whisper Bot is a Telegram bot designed to provide users with information about the video games and recommendations lists based on their preferences.

## Features

- **Game Information Retrieval**: Users can input the name of a video game, and the bot will retrieve information about it. The data will consist of the overview, genre, developer, metascore, userscore, available platforms and release date.

- **Game Recommendation**: Users can request a recommendation list with the video games based on their preferences. The more games user adds as an input, the more precise and suitable set of games will be returned.  

- **Unit Tests**: The project includes unit tests to ensure the reliability and correctness of the bot's functionalities.

## Technologies Used

- *Python* (as a main programming language)
- *pytelegrambotapi* (backend library for a bot)
- *Selenium WebDriver* (for accessing the appropriate game page on Metacritic)
- *BeautifulSoup* (a library for parsing the data about games)
- *unittest* (a library for unit tests during the whole development cycle)
- *ChatGPT API* (for returning the recommendations lists based on input)

## Usage

To use the Game Whisper Bot:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the bot using `python main.py`.
3. Interact with the bot through your Telegram account by searching for '@GameWhisperBot' and sending commands.