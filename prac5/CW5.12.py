N = int(input())
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
#FIXME
numbers = sorted(numbers)
print(numbers[len(numbers) // 2])