N = int(input())
Passengers = input().split()
for i in range(N):
    Passengers[i] = int(Passengers[i])
k = int(input())
rush_hours = 0
for i in range(N - k):
    if sum(Passengers[i: i + k]) > rush_hours:
        rush_hours = sum(Passengers[i: i + k])
print(rush_hours)