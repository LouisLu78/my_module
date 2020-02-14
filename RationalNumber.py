# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/14
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import math
from gcd import *

class RationalNumber:
    def __init__(self, numerator = 1, denominator = 2):
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
        return RationalNumber(new_nu, new_de)

    def __str__(self):
        if self.numerator == 0 or self.denominator == 1:
            return self.numerator

        elif self.numerator * self.denominator > 0:
            return '%d/%d' %(math.fabs(self.numerator), math.fabs(self.denominator))

        else:
            return '-%d/%d' %(math.fabs(self.numerator), math.fabs(self.denominator))

def _verify():
    rn_a = RationalNumber()
    print(rn_a)
    rn_b = RationalNumber(2, 3)
    print(rn_b)
    rn_c = RationalNumber(4, 7)
    a= rn_b + rn_a
    print(a)

if __name__=='__main__':
    _verify()


