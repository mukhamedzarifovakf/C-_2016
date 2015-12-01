def CountDebts(Debts, Bills):
    Debts[Bills[0]-1] -= Bills[2]
    Debts[Bills[1]-1] += Bills[2]
input = open('input.txt', 'r')
output = open('output.txt', 'w')
N, K = input.readline().split()
K = int(K)
N = int(N)
Debts = [0]*N
for i in range(K):
    Bills = [int(x) for x in input.readline().split()]
    CountDebts(Debts, Bills)
print(' '.join(map(str, Debts)), file = output)