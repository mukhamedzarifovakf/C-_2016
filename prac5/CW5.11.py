k, n = input().split()
k, n = int(k), int(n)
n_number = 1
if n > k:
    K_bonnachi = [1] * k
    for i in range(n - k + 1):
        K_bonnachi.append(sum(K_bonnachi[i: k + i]))
    n_number = K_bonnachi[n]
print(n_number)


