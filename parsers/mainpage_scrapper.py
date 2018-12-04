from bs4 import BeautifulSoup
import requests
import pickle

from tqdm import tqdm


def obtain_news(page):
    url = "https://www.reuters.com/news/archive?view=page&page={}&pageSize=10".format(page)
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    soup = soup.select_one(".module-content")
    stories = soup.select(".story")
    print(len(stories))
    news = []
    for i in range(len(stories)):
        link = stories[i].select_one(".story-content a").get("href")
        name = stories[i].select_one(".story-content a").text
        timestamp = stories[i].select_one(".timestamp").text
        news.append((link, timestamp))
    return news

iterator = tqdm(range(10))
news = []
for i in iterator:
    curr_news = obtain_news(i)
    news += curr_news
    iterator.set_description("{}".format(curr_news[-1][1]))

print(news)
print(len(news))
