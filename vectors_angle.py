# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/3
# If not explicitly pointed out, all the codes are written by myself.

def angle(x, y):
    import math
    list(x),list(y)
    if len(x)==2:
        x.append(0), y.append(0)
    dot=abs(sum(x[i]*y[i] for i in range(3)))
    abs_x=math.sqrt(sum(x[i]**2 for i in range(3)))
    abs_y = math.sqrt(sum(y[i] ** 2 for i in range(3)))
    cos_value=dot/(abs_x*abs_y)
    angle=math.acos(cos_value)
    return angle*180/math.pi


def _verify():
    x=(-1,0,1)
    y=(1,0,1)
    print(angle(x,y))

if __name__=='__main__':
    _verify()