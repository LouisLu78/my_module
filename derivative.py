# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/23

def derivative(f, x, h=1E-5):
    res=(f(x+h)-f(x))/h
    return res

def _verify():
    from math import cos, pi
    print('The derivative of cos(30) is %.4f.'%derivative(cos, pi/6))

if __name__=='__main__':
    _verify()
