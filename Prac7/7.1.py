from math import *
def formula1(x):
    if x != 1:
        a = (x ** 7 + 2 *(x ** 3) - 3 / (1 + x ** 2)) / (1 /(1 - x) + 21 / 8)
        return a
    else:
        return None

def formula2(x):
    if abs(x / (x ** 2 + 2)) <= 1 and x > 0:
        b = 1 /((sin(x / x ** 2 + 2)) ** 2 + exp(log1p(x) + 1))
        return b
    else:
        return None

def y(x):
    if x != 0:
        y = log((1 / (exp(sin(x) + 1))) / (1.25 + 1 / x ** 15), 1 + x ** 2)
        return y
    else:
        return None

print(y(1))
print(y(10))
print(y(1000))
