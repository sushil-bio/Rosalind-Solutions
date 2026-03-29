n, m = map(int, input().split())

F = [0] * (n + 1)
F[1] = F[2] = 1

for i in range(3, n + 1):
    if i <= m:
        F[i] = F[i - 1] + F[i - 2]
    else:
        F[i] = F[i - 1] + F[i - 2] - F[i - m]

print(F[n])
