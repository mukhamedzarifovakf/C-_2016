input = open('input.txt', 'r')
output = open('output.txt', 'w')
k, n = input.readline().split()
k, n = int(k), int(n)
First_year_tempreature = input.readline()
Minimums = [int(x) for x in First_year_tempreature.split()]
for i in range (k - 1):
    Current_year_tempretures = input.readline()
    Current_tempretures = [int(x) for x in Current_year_tempretures.split()]
    for i in range(n):
        if Minimums[i] > Current_tempretures[i]:
            Minimums[i] = Current_tempretures[i]
print(' '.join(map(str, Minimums)), file = output)