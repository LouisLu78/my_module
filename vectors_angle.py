# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/3
# If not explicitly pointed out, all the codes are written by myself.

def angle(x, y):
    import math
    x_list=list(x)
    y_list=list(y)
    if len(x_list)==2:
        x_list.append(0), y_list.append(0)
    dot=sum(x_list[i]*y_list[i] for i in range(3))
    abs_x=math.sqrt(sum(x_list[i]**2 for i in range(3)))
    abs_y = math.sqrt(sum(y_list[i]**2 for i in range(3)))
    cos_value=dot/(abs_x*abs_y)
    angle=math.acos(cos_value)
    return angle*180/math.pi


def _verify():
    # x=(-1,0,2)
    # y=(2,0,1)
    x=(5,-7)
    y=(-6,-4)
    print(angle(x,y))

if __name__=='__main__':
    _verify()