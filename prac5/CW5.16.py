N = int(input())
Pascal = [1]
print(' '.join(map(str, Pascal)))
for i in range(1, N + 1):
    Pascal.append(0)
    Pascal.insert(0, 0)
    New_Pascal = []
    for j in range(i + 1):
        New_Pascal.append(Pascal[j] + Pascal[j + 1])
    Pascal = New_Pascal
    print(' '.join(map(str, Pascal)))