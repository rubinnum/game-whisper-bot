import time
import logging
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import METACRITIC_URL
from game_data_page import GameDataPage

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def initiate_chrome_driver():
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


def accept_cookies(driver):
    accept_cookies_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    accept_cookies_button = driver.find_element(By.XPATH, accept_cookies_xpath)
    accept_cookies_button.click()


def find_the_game(driver, search_query):
    search_bar_xpath = '//*[@id="__layout"]/div/div[2]/header/div[1]/div/div[2]/div/div/form/input'
    search_bar = driver.find_element(By.XPATH, search_bar_xpath)
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)


def get_the_best_result(driver):
    best_result_xpath = '//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/a'
    best_result = driver.find_element(By.XPATH, best_result_xpath)
    best_result.click()
    time.sleep(2)


def extend_game_summary(driver):
    read_more_button_xpath = '//*[@id="__layout"]/div/div[2]/div[1]/div[6]/div/div/div[2]/div[1]/p/button'
    try:
        read_more_button = driver.find_element(By.XPATH, read_more_button_xpath)
        read_more_button.click()
        logging.info('The summary of a game was extended')
    except NoSuchElementException:
        logging.info('The summary of a game is fully displayed')


def get_game_data(game_name):
    driver = initiate_chrome_driver()
    driver.get(METACRITIC_URL)
    time.sleep(2)

    accept_cookies(driver)
    find_the_game(driver, game_name)
    get_the_best_result(driver)
    extend_game_summary(driver)

    game_data_page = GameDataPage(driver.page_source)

    game_data = {
        'summary': game_data_page.get_summary(),
        'userscore': game_data_page.get_userscore(),
        'metascore': game_data_page.get_metascore(),
        'genre': game_data_page.get_genre(),
        'platforms': game_data_page.get_platforms(),
        'release_date': game_data_page.get_release_date(),
        'developer': game_data_page.get_developer()
    }

    driver.quit()
    return game_data


def output_game_data(game_name):
    game_data = get_game_data(game_name)
    result = (
        f"Game summary: {game_data['summary']}\n"
        f"Game userscore: {game_data['userscore']}\n"
        f"Game metascore: {game_data['metascore']}\n"
        f"Game genre: {game_data['genre']}\n"
        f"Game platforms: {game_data['platforms']}\n"
        f"Game release: {game_data['release_date']}\n"
        f"Game developer: {game_data['developer']}\n"
    )
    return result

# Usage example
if __name__ == "__main__":
    game_name = input("Enter the name of the game: ")
    output_game_data(game_name)
