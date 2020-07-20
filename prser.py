import requests
from bs4 import BeautifulSoup as bs


def parse():
    URL = 'https://habr.com/ru/news/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = bs(response.content, 'html.parser')
    items = soup.findAll('article', class_='post post_preview')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('a', class_='post__title_link').get_text(strip=True)
        })

        for comp in comps:
            print(comp['title'])

parse()