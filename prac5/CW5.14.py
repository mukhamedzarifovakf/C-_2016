N = int(input())
A = []
B = []
for i in range(N):
    ai, bi = input().split()
    ai, bi = int(ai), int(bi)
    A.append(ai)
    B.append(bi)
time = int(input())
Passengers = 0
for i in range(N):
    if A[i] <= time and B[i] >= time:
        Passengers += 1
print(Passengers)