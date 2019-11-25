# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/25

class Central:
    def __init__(self,f,h=1E-5):
        self.f,self.h=f,h

    def __call__(self,x):
        f,h=self.f,self.h
        return (f(x+h) - f(x-h)) /(2*h)