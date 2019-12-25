# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/25
# If not explicitly pointed out, all the codes are written by myself.

import os, shutil
import PyPDF2
import docx

def count_txt(file):
    word_number=0
    with open(file,'r') as f:
        lines=f.readlines()
    for line in lines:
        word_number+=len(line.split())
    print('The txt_file consists of %d lines.'%len(lines))
    print('And it totally contains %d words,'%word_number, end=' ')
    print('which means each line is roughly composed of %.0f words.'%(word_number/len(lines)))

def count_docx(file):
    word_number = 0
    doc=docx.Document(file)
    for i in range(len(doc.paragraphs)):
        word_number+=len(str(doc.paragraphs[i].text).split())
    print('The doc_file consists of %d words.' %word_number)

def count_pdf(file):
    word_number = 0
    f= open(file,'rb')
    pdfreader=PyPDF2.PdfFileReader(f)
    for i in range(pdfreader.numPages):
        page=pdfreader.getPage(i)
        text=page.extractText()
        word_number += len(str(text))
    print('The pdf_file consists of %d words.' % word_number)

def _verify():
    files=[r'C:\Users\Basanwei\Exercise\ex\downfile.txt', r'D:\study\magicmethods.pdf',
           r'D:\Arbeiten\myfiles\Arbeiten\Downloads\email.docx']
    for file in files:
        path, filename=os.path.split(file)[0], os.path.split(file)[1]
        if filename.endswith('.txt'):
            count_txt(file)
        elif filename.endswith('.docx'):
            count_docx(file)
        elif filename.endswith('.pdf'):
            count_pdf(file)
        else:
            print('With our module, we currently donnot count the word number in this file type.')

if __name__=='__main__':
    _verify()