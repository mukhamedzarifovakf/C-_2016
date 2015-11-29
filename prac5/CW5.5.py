from random import randint
int_data = open('int_data.txt', 'w')
numbers = []
for i in range(10000):
    numbers.append(randint(0, 100))
print(' '.join(map(str, numbers)), file = int_data)


