jumps = input().split()
for i in range(len(jumps)):
    jumps[i] = int(jumps[i])
time = int(input())
for i in range(time):
    last = jumps.pop()
    jumps.insert(last, last)
print(jumps)
