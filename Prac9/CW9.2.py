def f(y, z):
    result = 108 - (815 - 1500 / z) / y
    return result
x0 = 4
x1 = 4.25
for i in range(30):
    x0, x1 = x1, f(x0, x1)
print(x1)