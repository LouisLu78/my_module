# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/7
# If not explicitly pointed out, all the codes are written by myself.

import requests, webbrowser
import shutil, os, random
import datetime

today=datetime.datetime.now()
Today=today.strftime('%Y_%m_%d')
newsfolder="F:\\Gstorage\\news"
if not os.path.exists(newsfolder):
    os.makedirs(newsfolder)

urls={'Yahoo':'http://news.yahoo.com','MSN':'http://www.msn.com/en-us/news/world',
    'FOX':'https://www.foxnews.com/world', 'AP':'https://apnews.com/apf-intlnews'}

for website in urls:
    res=requests.get(urls[website], stream=True)
    if res.status_code ==200:
        print('The website for {} is connected.'.format(website))
        with open('news.html', 'wb') as fnews:
            for chunk in res.iter_content(100000):
                fnews.write(chunk)
        filename=os.path.join(newsfolder, '{}_news_{}.html'.format(website, Today))
        shutil.move('news.html', filename)
        print('done')
    else:
        print('The internet connection for {} doesn\'t work today.'.format(website))

print('Enjoy yourself in reading today\'s news.')

newsurl=random.sample(list(urls.values()),2)
for url in newsurl:
    webbrowser.open(url)