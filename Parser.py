import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url):
        self.url = url

    def parse(self):
        from Main import Main  # импортируем модуль только в методе parse
        main = Main()
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', {'class': 'list-item'})

        for article in articles:
            title = article.find('a', {'class': 'list-item__title color-font-hover-only'}).text
            link = 'https://ria.ru' + article.find('a', {'class': 'list-item__title color-font-hover-only'})['href']
            print(title)
            print(link)
            print()