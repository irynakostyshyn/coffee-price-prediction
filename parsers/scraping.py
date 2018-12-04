import os
import time
import json
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager, cpu_count

from datetime import timedelta, datetime
from tqdm import tqdm

def valid_dates():
    import pandas as pd
    data = pd.read_csv('full_data.csv')

    return data['date']

def download_file(args):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'UserAgent': 'Mozilla / 5.0(X11;Ubuntu;Linux x86_64;rv: 63.0) Gecko / 20100101 Firefox / 63.0',
               'Cookie': 'ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22ad9ea703-228f-401f-813b-0250cc69aec1%22; _cb_ls=1; _ga=GA1.2.673432093.1541412268; _gid=GA1.2.273007591.1541412268; __tbc=%7Bjzx%7Dyo9xUxAKwg32SeQvuAZGbd7nobfKUvmIye6IuCPVBcx1umVbi4Si0YEaqTbehUkBEnQiJwTFLMckOKvhIiZfxZlo1w2OVpLhpF26vrlAHp73fw51B0kaCbaEKL83a4rYHzyVzbU0qDL8Htc3rl51Vg; __pat=-18000000; __pvi=%7B%22id%22%3A%22v-2018-11-05-15-09-21-498-zAWNKiwLDHw70fDE-98cd3bcf7c0c5951ba50f79b6508f949%22%2C%22domain%22%3A%22.reuters.com%22%2C%22time%22%3A1541423361498%7D; xbc=%7Bjzx%7DBtS3PHr8KcpV6uj81Rx7DABVMccyC_xq_1VPUP4eVVMcR0nrm5-pcBSNAzdX2mk36d8mimHtHZe5l6HkT7ijdI42vfARtPY5wVcV-ORPJVwogNekqF_EMGuFVqmMRYPK; AAMC_reuters_0=REGION%7C6; aam_uuid=26295770404178660713028812129756778203; _cb=B71vD-Cu3mHcmL3ZT; _chartbeat2=.1541412270848.1541423365414.1.DkkfTiUtbeSBwuSrJ0QbsrDbv26M.1; nativeAiInstallationId=d0c74277-6e02-4e98-abcf-240c2bbe214d; mnet_session_depth=1%7C1541423361995; D_DUID=5a61c0f0-f055-402e-b9f5-be54b9b55896; D_TOKEN=1.0:cd55232adccbb147cfdb52900e84280f:94ee5cb07f7998a650d72bad93fed3d74468e68629c19e325a2f9bc0a1b67b87a16c070fd7c36c9fa0a43d3bca4733eb7afdf870cf4b372c038193f182a87d8c23ee6cc38aa01e84d2ac22ac92415a88771f07ebff87cc767b887089b5cc5e89d3b983c0fe1072d05db06ff8fa8548cee09a5af659e85a84e1885cb136bb8043:2781abd6f1d319f5e76b24186a182447e9f73fe6c44edf4721765bda3f56f336; nativeAiSession=NWFjOGY5YTItNjkzYi00NDIyLWI5ZTEtZDY5Yjk2NGYyNDBlfA==; _cb_svref=null; _gali=header; _gat=1'}
    cookie = {
        'ajs_user_id' : 'null',
        'ajs_group_id': 'null',
        'ajs_anonymous_id': '%22ad9ea703-228f-401f-813b-0250cc69aec1%22',
        '_cb_ls' : '1',
        '_ga' : 'GA1.2.673432093.1541412268',
        '_gid' : 'GA1.2.273007591.1541412268',
        '__tbc' : '%7Bjzx%7Dyo9xUxAKwg32SeQvuAZGbd7nobfKUvmIye6IuCPVBcx1umVbi4Si0YEaqTbehUkBEnQiJwTFLMckOKvhIiZfxZlo1w2OVpLhpF26vrlAHp73fw51B0kaCbaEKL83a4rYHzyVzbU0qDL8Htc3rl51Vg',
        '__pat' : '-18000000',
        '__pvi' : '%7B%22id%22%3A%22v-2018-11-05-15-09-21-498-zAWNKiwLDHw70fDE-98cd3bcf7c0c5951ba50f79b6508f949%22'
                  '%2C%22domain%22%3A%22.reuters.com%22%2'
                  'C%22time%22%3A1541423361498%7D',
        'xbc': '%7Bjzx%7DBtS3PHr8KcpV6uj81Rx7DABVMccyC_xq_1VPUP4eVVMcR0nrm5-pcBSNAzdX2mk36d8mimHtHZe5l6HkT7ijdI42vfARtPY5wVcV-ORPJVwogNekqF_EMGuFVqmMRYPK',
        'AAMC_reuters_0' : 'REGION%7C6',
        'aam_uuid' : '26295770404178660713028812129756778203',
        '_cb' : 'B71vD - Cu3mHcmL3ZT',
        '_chartbeat2' : '.1541412270848.1541423365414.1.DkkfTiUtbeSBwuSrJ0QbsrDbv26M.1',
        'nativeAiInstallationId' : 'd0c74277 - 6e02 - 4e98 - abcf - 240c2bbe214d' ,
        'mnet_session_depth' : '1 % 7C1541423361995',
        'D_DUID' : '5a61c0f0 - f055 - 402e - b9f5 - be54b9b55896',
        'D_TOKEN' : '1.0:cd55232adccbb147cfdb52900e84280f: 94ee5cb07f7998a650d72bad93fed3d74468e68629c19e325a2f9bc0a1b67'
                    'b87a16c070fd7c36c9fa0a43d3bca4733eb7afdf870cf4b372c038193f182a87d8c23ee6cc38aa01e84d2ac22ac92415a88'
                    '771f07ebff87cc767b887089b5cc5e89d3b983c0fe1072d05db06ff8fa8548cee09a5af659e85a84e1885cb136bb8043:'
                    ' 2781abd6f1d319f5e76b24186a182447e9f73fe6c44edf4721765bda3f56f336',
        'nativeAiSession' : 'NWFjOGY5YTItNjkzYi00NDIyLWI5ZTEtZDY5Yjk2NGYyNDBlfA==',
        '_cb_svref' : 'null',
        '_gali' :' header',
        '_gat': '1'

    }
    url, out_dir, my_dict = args
    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookie)
    #session.get(url)
    response = session.get(url)

    html_doc = response.text
    #print(html_doc)
    filename = os.path.join(out_dir, url[url.rfind("/") + 1:] + ".html")
    soup = BeautifulSoup(html_doc, 'html.parser')

    tag = soup.select_one(".StandardArticleBody_body")
    not_found = soup.select_one("#sectionTitle")
    if tag != None:
        my_dict[filename] = tag.text
    elif not_found:
        print(url, not_found.text)
    else:
        print(url, "Error")

def retrieve_links(date):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, br',
               'UserAgent':'Mozilla / 5.0(X11;Ubuntu;Linux x86_64;rv: 63.0) Gecko / 20100101Firefox / 63.0',
               'Cookie': 'ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22ad9ea703-228f-401f-813b-0250cc69aec1%22; _cb_ls=1; _ga=GA1.2.673432093.1541412268; _gid=GA1.2.273007591.1541412268; __tbc=%7Bjzx%7Dyo9xUxAKwg32SeQvuAZGbd7nobfKUvmIye6IuCPVBcx1umVbi4Si0YEaqTbehUkBEnQiJwTFLMckOKvhIiZfxZlo1w2OVpLhpF26vrlAHp73fw51B0kaCbaEKL83a4rYHzyVzbU0qDL8Htc3rl51Vg; __pat=-18000000; __pvi=%7B%22id%22%3A%22v-2018-11-05-13-53-29-304-dZUexncZUxTRTp9y-7e5eed9358ce06131470ad714e0da820%22%2C%22domain%22%3A%22.reuters.com%22%2C%22time%22%3A1541419527651%7D; xbc=%7Bjzx%7DBtS3PHr8KcpV6uj81Rx7DABVMccyC_xq_1VPUP4eVVMcR0nrm5-pcBSNAzdX2mk36d8mimHtHZe5l6HkT7ijdI42vfARtPY5wVcV-ORPJVwogNekqF_EMGuFVqmMRYPK; AAMC_reuters_0=REGION%7C6; aam_uuid=26295770404178660713028812129756778203; _cb=B71vD-Cu3mHcmL3ZT; _chartbeat2=.1541412270848.1541419531674.1.R6d7qDVq_fRBg1wYHD6BWL48OE6m.10; nativeAiInstallationId=d0c74277-6e02-4e98-abcf-240c2bbe214d; mnet_session_depth=11%7C1541418810352; D_DUID=5a61c0f0-f055-402e-b9f5-be54b9b55896; D_TOKEN=1.0:cd55232adccbb147cfdb52900e84280f:94ee5cb07f7998a650d72bad93fed3d74468e68629c19e325a2f9bc0a1b67b87a16c070fd7c36c9fa0a43d3bca4733eb7afdf870cf4b372c038193f182a87d8c23ee6cc38aa01e84d2ac22ac92415a88771f07ebff87cc767b887089b5cc5e89d3b983c0fe1072d05db06ff8fa8548cee09a5af659e85a84e1885cb136bb8043:2781abd6f1d319f5e76b24186a182447e9f73fe6c44edf4721765bda3f56f336; nativeAiSession=NmZiNGYwZTEtYWIzOC00MzlhLWIyYjYtNDVmZGNjZjExZWZjfA==; _cb_svref=null; _gat=1'}
    url = "https://www.reuters.com/resources/archive/us/{}.html".format(date)
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url)
    print(session.headers)
    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    links = soup.select(".headlineMed a")
    urls2parse = []
    for link in links:
        url = link.get("href")
        if not url.startswith("http://www.reuters.com/news/video/videoStory?storyID="):
            urls2parse.append(url)
    return urls2parse


def json_save(my_dict, out_dir):
    f = open("{}/j.txt".format(out_dir), "w")
    f.write(str(my_dict))
    f.close()



if __name__ == "__main__":
    cpu_count = cpu_count() * 4
    dates = valid_dates()
    start = time.time()
    for i in range(17, 35):
        date = dates[i].replace('-', '')
        urls2parse = retrieve_links(date)
        print(urls2parse)
        out_dir = "./data/" + date
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        manager = Manager()
        my_dict = manager.dict()
        args = [(url, out_dir, my_dict) for url in urls2parse]
        with Pool(cpu_count) as p:
            p.map(download_file, args)
        print(my_dict)
        d = my_dict._getvalue()
        print(time.time() - start)
        print(len(d), len(urls2parse))
        json_save(my_dict, out_dir)




