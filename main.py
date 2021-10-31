from bs4 import BeautifulSoup
import requests
from pprint import pprint

base_url = "https://habr.com"
url = "https://habr.com/ru/all/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

KEYWORDS = ['JavaScript', 'C++', 'ReactJS', 'python']

list_stat = list()

def parse_url_tags(url, keywords, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        container = soup.select_one(".tm-articles-list")


        for item_pr in container.select('article.tm-articles-list__item'):
            dates = item_pr.select_one(".tm-article-snippet__datetime-published").text
            name = item_pr.select_one(".tm-article-snippet__title-link span").text
            link = base_url + item_pr.select_one(".tm-article-snippet__title-link").attrs["href"]

            list_tag_item_container = item_pr.select_one('.tm-article-snippet__hubs')
            list_tag_item = list()
            for item_tag in list_tag_item_container.select('.tm-article-snippet__hubs-item'):
                list_tag_item.append(item_tag.text.replace(' *', ''))


            result_search = list(set(KEYWORDS) & set(list_tag_item))

            if not result_search:
                pass
            else:
                print(dates + ' | ' + name + ' | ' + link)

    else:
        print('Ошибка ответа сервера')

    return


if __name__ == '__main__':
    parse_url_tags(url, KEYWORDS, headers)

