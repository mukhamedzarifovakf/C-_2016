from fractions import Fraction as f
def g(number, x0 = 4, x1 = 4.25):
    x0 = f(x0, 1)
    x1 = f(int(x1 * 100), 100)
    for i in range(number):
        x2 = f(108, 1) - f(f(815, 1) - f(f(1500, 1), x1), x0)
        x0, x1 = x1, x2
    print(x0, x1)
g(2)