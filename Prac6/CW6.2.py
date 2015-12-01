input = open('input.txt', 'r')
output = open('output.txt', 'w')
N, n = input.readlines()
N = int(N.rstrip())
n = n.rstrip()
n = [int(x) for x in n.split()]
requiredcoins = 0
availiblecoins = 0
for i in range(N):
    if n[i] == 5:
        availiblecoins += 1
    else:
        availiblecoins -= (n[i] - 5) / 5
        if availiblecoins < 0:
            requiredcoins -= availiblecoins
            availiblecoins = 0
print(int(requiredcoins), file = output)