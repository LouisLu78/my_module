# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/29
# If not explicitly pointed out, all the codes are written by myself.
import pdfkit

path_wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def url_to_pdf(url, pdf_file):
    pdfkit.from_url(url, pdf_file, configuration=config)
    print('done')

def html_to_pdf(html, pdf_file):
    pdfkit.from_file(html, pdf_file, configuration=config)
    print('done')



def _verify():
    import os, requests

    url='https://mp.weixin.qq.com/s/Q6Fi1nufZejfwaBjFIYu1Q'
    pdffolder = "C:\\Users\\Basanwei\\Downloads\\pdf"
    if not os.path.exists(pdffolder):
        os.makedirs(pdffolder)
    pdf_file=os.path.join(pdffolder,'tmp.pdf')
    url_to_pdf(url,pdf_file)

    res=requests.get('https://mp.weixin.qq.com/s/rVHeF_DzY53Zceb0nHo6_Q')
    res.raise_for_status()
    html_file = os.path.join(pdffolder, 'tmp1.html')
    with open(html_file,'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)
    pdf_file1 = os.path.join(pdffolder, 'tmp1.pdf')
    html_to_pdf(html_file,pdf_file1)

if __name__=='__main__':
    _verify()