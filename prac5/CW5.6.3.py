float_data = open('float_data.txt', 'r')
a = float_data.readlines()
for i in range(0, len(a)):
    a[i] = a[i].rstrip()
    a[i] = float(a[i])
nmax = a.index(max(a))
nmin = a.index(min(a))
print(nmax, nmin)
