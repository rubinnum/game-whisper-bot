import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants import METACRITIC_URL
from game_data_page import GameDataPage


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


def find_the_game(search_query, driver):
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


def get_game_data(game_name):
    driver = initiate_chrome_driver()
    driver.get(METACRITIC_URL)

    accept_cookies(driver)
    find_the_game(game_name, driver)
    get_the_best_result(driver)

    game_data_page = GameDataPage(driver.page_source)

    game_data = {
        'userscore': game_data_page.get_userscore(),
        'metascore': game_data_page.get_metascore()
    }

    driver.quit()
    return game_data


# Usage example
if __name__ == "__main__":
    game_name = input("Enter the name of the game: ")
    game_data = get_game_data(game_name)
    print('Game userscore: ', game_data['userscore'])
    print('Game metascore: ', game_data['metascore'])
