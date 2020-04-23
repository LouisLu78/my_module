# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/14
# Email: gq4350lu@hotmail.com

import math
from gcd import *

class Fraction:

    def __init__(self, numerator = 1, denominator = 1):
        if denominator == 0:
            raise Exception("The denominator cannot be zero, please reenter another number!")
        else:
            g = gcd(numerator, denominator)
            self.numerator = numerator / g
            self.denominator = denominator / g

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __add__(self, other):
        new_nu = self.numerator * other.denominator + self.denominator * other.numerator
        new_de = self.denominator * other.denominator
        return Fraction(new_nu, new_de)

    def __sub__(self, other):
        new_nu = self.numerator * other.denominator - self.denominator * other.numerator
        new_de = self.denominator * other.denominator
        return Fraction(new_nu, new_de)

    def __mul__(self, other):
        new_nu = self.numerator * other.numerator
        new_de = self.denominator * other.denominator
        return Fraction(new_nu, new_de)

    def __floordiv__(self, other):
        new_nu = self.numerator * other.denominator
        new_de = self.denominator * other.numerator
        return Fraction(new_nu, new_de)

    def __str__(self):
        if self.numerator == 0 or self.denominator == 1:
            return '%d' %self.numerator

        elif self.numerator * self.denominator > 0:
            return '%d/%d' %(math.fabs(self.numerator), math.fabs(self.denominator))

        else:
            return '-%d/%d' %(math.fabs(self.numerator), math.fabs(self.denominator))

def _verify():
    rn_a = Fraction()
    print(rn_a)
    rn_b = Fraction(2, 3)
    print(rn_b)
    rn_c = Fraction(4, 7)
    s= rn_b - rn_a
    print(s)
    m = rn_b // rn_c
    print(m)
    if rn_b > rn_c:
        print('rn_b is greater.')
    else:
        print('rn_c is greater.')
    print(rn_b > rn_a)

if __name__ == '__main__':
    _verify()


