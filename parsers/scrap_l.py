import json
import requests
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from tqdm import tqdm
import numpy as np

def obtain_links(date):
    archive_url = "https://www.reuters.com/resources/archive/us/{}.html".format(date)
    params = {"url": archive_url}
    r = requests.get("http://archive.org/wayback/available", params=params)
    data = json.loads(r.text)
    if "closest" in data["archived_snapshots"] :
        backup_url = data["archived_snapshots"]["closest"]["url"]
        backup_r = requests.get(backup_url)
        html_doc = backup_r.text

        soup = BeautifulSoup(html_doc, 'html.parser')
        links = soup.select(".headlineMed a")
        urls2parse = []
        for link in links:
            url = link.get("href")
            url = url[url.find("http://www.reuters.com"):]
            if not url.startswith("http://www.reuters.com/news/video/videoStory?storyID="):
                urls2parse.append(url)
        # print(len(urls2parse))
        return urls2parse
    else:
        # print("this link is not available")
        return []


# print()

def valid_dates():
    import pandas as pd
    data = pd.read_csv('full_data.csv')

    return np.array(data['date'])


delta = timedelta(days=1)
time = datetime(2014, 1, 1)
v_links = dict()
dates = valid_dates()

iterator = tqdm(dates)

for date in iterator:
    iterator.set_description('Amount {}'.format(len(v_links)))

    date = date.replace('-', '')
    new_links = obtain_links(date)
    if new_links:
        if date in v_links:
            v_links[date] += new_links
        else:
            v_links[date] = new_links
    time += delta

print()
print(len(v_links), v_links)
