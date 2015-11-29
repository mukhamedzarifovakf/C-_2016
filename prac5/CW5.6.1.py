float_data = open('float_data.txt', 'r')
a = float_data.readline()
a = a.split()
for i in range(len(a)):
    a[i] = float(a[i])
average = sum(a) / len(a)
print(average)
