import requests
from bs4 import BeautifulSoup
import re


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'теперь', 'США', 'asterisk']
keyword_set =set([keyword.lower() for keyword in  KEYWORDS])
response = requests.get('https://habr.com/ru/all/')
bs = BeautifulSoup(response.text, 'html.parser')

articles = bs.find_all(class_="content-list__item content-list__item_post shortcuts_item")
for article in articles:
    post = list(map(lambda p: p.text, article.find_all('article', class_='post')))
    output_list = []
    if post:
        pattern = r"[«]+|\\+\w?|(\s+|[»]+|\.+|\,)"
        regex = re.compile(pattern)
        result = regex.sub(" ", post[0]).split(' ')
        result_lower = set([x.lower() for x in result])


        if keyword_set.intersection(result_lower):
            href_ = article.find('a', class_="post__title_link")
            link = href_.attrs.get('href')
            datatime = article.find('span', class_="post__time")
            title = article.find('a', class_="post__title_link")
            output_list.extend([datatime.text, title.text, link])
            print(' - '.join(output_list))
