# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/3
# If not explicitly pointed out, all the codes are written by myself.

def angle(x, y):
    import numpy as np
    if len(x)!=len(y):
        raise Exception('The two vectors have unequal numbers of dimensions!' )
    X=np.array(x)
    Y=np.array(y)

    dot=np.dot(X,Y)
    abs_x=np.sqrt(sum(X[i]**2 for i in range(len(X))))
    abs_y = np.sqrt(sum(Y[i]**2 for i in range(len(Y))))
    cos_value=dot/(abs_x*abs_y)
    angle=np.arccos(cos_value)
    return angle*180/np.pi


def _verify():
    # x=(-1,0,2)
    # y=(2,0,1)
    x=(5,-7)
    y=(-6,-4)
    print(angle(x,y))

if __name__=='__main__':
    _verify()


