from random import randint
float_data = open('float_data.txt', 'w')
numbers = []
for i in range(10000):
    numbers.append(randint(0, 10000) / 100)
print(' '.join(map(str, numbers)), file = float_data)