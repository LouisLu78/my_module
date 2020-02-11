# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/25
# If not explicitly pointed out, all the codes are written by myself.

import os
import PyPDF2
import docx

def count_txt(file):
    word_number = 0
    with open(file,'r') as f:
        lines = f.readlines()
    for line in lines:
        word_number += len(line.split())
    print('The file of {} consists of {} lines.'.format(os.path.basename(file), len(lines)))
    print('And it totally contains %d words,'%word_number, end=' ')
    print('which means each line is roughly composed of %.1f words.'%(word_number/len(lines)))

def count_docx(file):
    word_number = 0
    doc=docx.Document(file)
    for p in doc.paragraphs:
        word_number += len(p.text.split())
    print('The file of {} consists of {} words.'.format(os.path.basename(file), word_number))

def count_pdf(file):
    word_number = 0
    f = open(file,'rb')
    pdfreader = PyPDF2.PdfFileReader(f)
    for i in range(pdfreader.numPages):
        page = pdfreader.getPage(i)
        text = page.extractText()
        word_number += len(text.split())

    print('The file of %s consists of %d words.'%(os.path.basename(file), word_number))

def _verify():
    files = [r'C:\Users\Basanwei\Exercise\ex\downfile.txt', r'D:\study\magicmethods.pdf',
           r'D:\Arbeiten\myfiles\Arbeiten\Downloads\email.docx',
           r'D:\book\Physical Chemistry of Polymer Solutions - Theoretical Background.pdf']
    for file in files:
        path, filename = os.path.split(file)[0], os.path.split(file)[1]
        if filename.endswith('.txt'):
            count_txt(file)
        elif filename.endswith('.docx'):
            count_docx(file)
        elif filename.endswith('.pdf'):
            count_pdf(file)
        else:
            print('With our module, we currently do not count the word number for this file type.')

if __name__ == '__main__':
    import time
    start = time.time()
    _verify()
    end = time.time()
    print('The counting costs %.2f seconds.'%(end-start))