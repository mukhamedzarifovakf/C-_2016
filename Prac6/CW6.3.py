input = open('input.txt', 'r')
output = open('output.txt', 'w')
N, Slippers = input.readlines()
N = int(N.rstrip())
Slippers = [int(x) for x in Slippers.split()]
Distance = 0
for i in range(N-1):
    if Slippers[i] < 0:
        for k in range(i+1, N):
            if Slippers[k] == -Slippers[i] and Distance == 0:
                Distance = k - i
            elif Slippers[k] == -Slippers[i] and Distance > k - i:
                Distance = k - i
print(Distance, file = output)