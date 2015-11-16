A = set(input())
B = set(input())
for x in A:
    if x not in B:
        print(x, end = ' ')