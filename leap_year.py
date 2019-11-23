# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:20191121

def isleap(y):

    if y%100==0:
       if y%400==0:
           return True
       else:
           return False
    elif y%4==0:
        return True
    else:
        return False

def _verify():
    year=[1978,1996,2000,2019,2020]
    for y in year:
        if isleap(y):
            print('Year %d is a leap year!'%y)
        else:
            print('Year %d is NOT a leap year.' %y)

if __name__=='__main__':
    _verify()
