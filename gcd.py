# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/14
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def _verify():
    x, y = 45, 35
    print("The greatest common divisor of %d and %d is %d." % (x, y, gcd(x, y)))


if __name__ == "__main__":
    _verify()
