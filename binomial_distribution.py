# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019:11:19:21:19

'''
The following programs are the answers to the questions in book <A Primer on Scientific Programming with Python
Third Edition> by Hans Petter Langtangen. I wrote all the codes myself. Below is exercise 4.24.
Throwing a die can be another example, if (e.g.) getting a six is considered success and all other outcomes represent failure. Let the probability of success be p and that of failure 1−p.
 If we perform n experiments, where the outcome of each experiment does not depend on the outcome of previous experiments, the probability of getting success
x times (and failure n − x times) is given by formula 4.8. This formula (4.8) is called the binomial distribution. The expression
x! is the factorial of x as defined in Exercise 3.19. Implement (4.8) in a function binomial(x, n, p). Make a module containing this binomial
function. Include a test block at the end of the module file.
'''
def binomial(x, n, p):
    from math import factorial
    c=factorial(n)/(factorial(x)*factorial(n-x))
    possibilities=p**x*(1-p)**(n-x)
    return c*possibilities

def _verify():
    '''
    suppose we throw a die 100 times with 20 times we get "6-point", obviously in this case success is 1/6.
    '''
    x, n, p=20, 100, 1/6
    result=binomial(x,n,p)
    print('We played %d times with obtaining the six for %d times and the propbability is %9.3E.'%(n,x,result))

if __name__ == '__main__':
    _verify()
