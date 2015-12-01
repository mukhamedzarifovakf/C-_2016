input = open('input.txt', 'r')
output = open('output.txt', 'w')
N, n = input.readlines()
N = N.rstrip()
N = int(N)
n = n.rstrip()
n = n.split()
for i in range(N-1):
    for k in range(i+1, N):
        if n[k] == n[i]:
            print(n[i], file = output)