Emin = 1
while Emin > 0:
    if 2 ** (-Emin - 1) + 1 == 1 and 2 ** (-Emin) != 0:
        break
    else:
        Emin += 1
e = 2 ** (-Emin)
print(e)