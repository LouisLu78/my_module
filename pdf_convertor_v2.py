# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/30
# If not explicitly pointed out, all the codes are written by myself.
import pdfkit
import os

class Convertor:
    counter=0

    def __init__(self):
        Convertor.counter+=1
        self.path_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        self.config=pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltopdf)
        if not os.path.exists('.\\temp'):
            os.mkdir('.\\temp')

        self.pdf_file='.\\temp\\tmp{}.pdf'.format(Convertor.counter)

    def url_to_pdf(self, url):
        pdfkit.from_url(url, self.pdf_file, configuration=self.config)
        print('done')

    def html_to_pdf(self, html):
        pdfkit.from_file(html, self.pdf_file, configuration=self.config)
        print('done')

    def string_to_pdf(self, string):
        pdfkit.from_string(string, self.pdf_file, configuration=self.config)
        print('done')


c=Convertor()
c.url_to_pdf('https://mp.weixin.qq.com/s/gJZWwyiYuQlhrKOrF0BMaQ')