from math import sqrt

def f(x):
    return sqrt(x)

def d(a, h):
    return ( f(a + h) - f(a) ) / h

a = 3
print(d(a, 0.1))
print(d(a, 0.01))
print(d(a, 0.001))
