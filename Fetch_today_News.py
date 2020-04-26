# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/7
# If not explicitly pointed out, all the codes are written by myself.

import datetime, os, random
import shutil, threading

import requests
import webbrowser


def fetch_news():
    today = datetime.datetime.now()
    Today = today.strftime('%Y_%m_%d')
    newsfolder = "F:\\Gstorage\\news"
    if not os.path.exists(newsfolder):
        os.makedirs(newsfolder)

    for website in urls:
        res = requests.get(urls[website], stream=True)
        if res.status_code != 200:
            print('The internet connection for {} doesn\'t work today.'.format(website))
            continue

        else:
            print('The website for {} is connected.'.format(website))
            with open('news.html', 'wb') as fnews:
                for chunk in res.iter_content(100000):
                    fnews.write(chunk)
            filename = os.path.join(newsfolder, '{}_news_{}.html'.format(website, Today))
            shutil.move('news.html', filename)
            print('done')


def open_url():
    newsurl = random.sample(list(urls.values()), 2)
    for url in newsurl:
        webbrowser.open(url)


def _verify():
    global urls
    urls = {'Yahoo': 'http://news.yahoo.com', 'MSN': 'http://www.msn.com/en-us/news/world',
            'FOX': 'https://www.foxnews.com/world', 'AP': 'https://apnews.com/apf-intlnews'}
    t1 = threading.Thread(target=fetch_news)
    t2 = threading.Thread(target=open_url)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    _verify()
    print('Enjoy yourself in reading today\'s news.')
