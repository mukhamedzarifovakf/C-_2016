a = open('int_data.txt', 'r')
a = a.readlines()
for i in range(0, len(a)):
    a[i] = a[i].rstrip()
    a[i] = int(a[i])
for i in range (0, len(a)//2):
    print(a[i], a[len(a) - i - 1], end = ' ')
if len(a) % 2 == 1:
    print(a[len(a)//2])
