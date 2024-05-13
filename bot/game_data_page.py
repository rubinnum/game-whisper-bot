from bs4 import BeautifulSoup


class GameDataPage:
    def __init__(self, page_source):
        self.soup = BeautifulSoup(page_source, 'html.parser')

    def __get_score_elements(self):
        scores_parent = self.soup.find("div", class_="c-productHero_scoreInfo")
        scores = scores_parent.find_all("div", class_="c-productScoreInfo_scoreNumber")
        return scores

    def get_metascore(self):
        scores = self.__get_score_elements()
        metascore_span = scores[0].find("span")
        return metascore_span.text if metascore_span else 'Was not found'

    def get_userscore(self):
        scores = self.__get_score_elements()
        userscore_span = scores[1].find("span")
        return userscore_span.text if userscore_span else 'Was not found'
