import math
float_data = open('float_data.txt', 'r')
a = float_data.readline()
a = a.split()
for i in range(len(a)):
    a[i] = float(a[i])
average = sum(a) / len(a)
b = []
for i in range(0, len(a)):
    b.append(a[i] ** 2)
mistake = math.sqrt(sum(b) / len(b) - average **2)
print(mistake)
