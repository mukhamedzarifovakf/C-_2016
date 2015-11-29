int_data = open('int_data.txt', 'r')
a = int_data.readlines()
for i in range(0, len(a)):
    a[i] = a[i].rstrip()
    a[i] = int(a[i])
b = []
for i in range(0, max(a)+1, 1):
    b.append(a.count(i))
b.pop(0)
print(b.index(max(b)) + 1, b.index(min(b)) + 1)
