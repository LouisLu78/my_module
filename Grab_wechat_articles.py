# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/1
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import bs4, requests
import re, os, threading
from pdf_convertor import *

def downfile(start, end):

    for i in range(start, end):
        pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
        pdffile = os.path.join(pdffolder, "%s.pdf" %urls[i][1])
        url_to_pdf(urls[i][0],pdffile)

        print('The No.%d file is downloaded.' %i)


def main(original_url):
    global urls
    downthreads,urls= [],[]

    res=requests.get(original_url)
    res.raise_for_status()
    with open('article104.html', 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)

    f=open('article104.html','r', encoding='UTF-8')
    soup=bs4.BeautifulSoup(f.read(),'html.parser')
    regex = re.compile(r'\W')
    tags=soup.find_all(class_="article_access")
    for tag in tags:
        text=regex.sub('_', tag.text)
        urls.append((tag['href'],text))

    for i in range(0,len(urls),20):
        downthread=threading.Thread(target=downfile, args=(i, i+20))
        downthreads.append(downthread)
        downthread.start()

    for t in downthreads:
        t.join()
    print('The download task finished.')

if __name__=="__main__":
    url='https://mp.weixin.qq.com/s/D6w2bmdH5SyAYioIDIHEvg'
    main(url)