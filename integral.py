# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/11/23

class Integral:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n

    def trapezoidal(self, f, a, x, n):

        h = (x - a) / n
        I = 0.5 * f(a)
        for i in range(1, n):
            I += f(a + i * h)
        I += 0.5 * f(x)
        I *= h
        return I

    def __call__(self, x):
        return self.trapezoidal(self.f, self.a, x, self.n)

def _verify():

    f=lambda x: 2*x**2
    G=Integral(f,0,n=100)
    result=G(10)
    print(result)

if __name__=='__main__':
    _verify()
