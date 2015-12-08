int_data = open('int_data.txt', 'r')
a = int_data.readline()
for i in range(0, len(a)):
    a[i] = a[i].rstrip()
    a[i] = int(a[i])
b = []
for i in range(0, max(a)+1, 1):
    b.append(a.count(i))
for i in range(1, len(b)):
    print(i, b[i])
