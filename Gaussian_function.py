# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:
def Gaussian_func(m, s, x):

    from math import sqrt, exp, pi

    p=1/((sqrt(2*pi))*s)
    i=((x-m)/s)**2
    return p*exp(-0.5*i)

def _verify():
    m,s,x=1,10,-1
    result=Gaussian_func(m,s,x)
    print('The result of Gaussion function is %.4f.'%result)

if __name__=='__main__':
    _verify()