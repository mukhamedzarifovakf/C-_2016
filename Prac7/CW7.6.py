import numpy as np
import matplotlib.pyplot as plt
with open('input.txt', 'r') as inp:
    data = {}
    n = 0
    length = 0
    while True:
        a = inp.readline()
        if a == '':
            break
        a = a.split()
        for word in a:
            if len(word) in data:
                data[len(word)] += 1
            else:
                data[len(word)] = 1
            n += 1
            length += len(word)
    print(data, length/n)

objects = ('',)
performance = [0]
for i in range(int(2*length/n)):
    objects = objects + (str(i+1), )
    if i+1 in data:
        performance.append(data[i+1])
    else:
        performance.append(0)
y_pos = np.arange(len(objects))


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Value')
plt.title('Bar title')

plt.show()