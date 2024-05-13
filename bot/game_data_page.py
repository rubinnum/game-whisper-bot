from bs4 import BeautifulSoup


class GameDataPage:
    def __init__(self, page_source):
        self.soup = BeautifulSoup(page_source, 'html.parser')

    def get_summary(self):
        game_description = self.soup.find('span', class_='c-productionDetailsGame_description').get_text(strip=True)
        if game_description.endswith('...'):
            game_description = game_description[:-len('...')]
        return game_description

    def __get_score_elements(self):
        scores_parent = self.soup.find('div', class_='c-productHero_scoreInfo')
        scores = scores_parent.find_all('div', class_='c-productScoreInfo_scoreNumber')
        return scores

    def get_metascore(self):
        scores = self.__get_score_elements()
        metascore_span = scores[0].find('span')
        return metascore_span.get_text() if metascore_span else 'Was not found'

    def get_userscore(self):
        scores = self.__get_score_elements()
        userscore_span = scores[1].find('span')
        return userscore_span.get_text() if userscore_span else 'Was not found'

    def get_genre(self):
        list_of_genres = self.soup.find('ul', class_='c-genreList')
        genre_span = list_of_genres.find('span')
        return genre_span.get_text(strip=True) if genre_span else 'Was not found'

    def get_platforms(self):
        list_of_platforms = self.soup.find('div', class_='c-gameDetails_Platforms').find('ul')
        platforms = list_of_platforms.find_all('li')
        available_platforms = []
        for platform in platforms:
            available_platforms.append(platform.get_text(strip=True))
        return available_platforms

    def get_release_date(self):
        release_date_container = self.soup.find('div', class_='c-gameDetails_ReleaseDate')
        release_date = release_date_container.find_all('span')[1]
        return release_date.get_text(strip=True)

    def get_developer(self):
        developer = self.soup.find('div', class_='c-gameDetails_Developer').find('li').get_text(strip=True)
        return developer
