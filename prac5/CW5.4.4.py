A = [1, 2, 3, 2, 3, 3]
max = 1
n = A[0]
for elem in A:
    if A.count(elem) > max:
        max = A.count(elem)
        n = elem
print(n)
