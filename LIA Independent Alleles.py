import math

k, N = map(int, input().split())

total = 2 ** k
p = 0.25

ans = 0

for i in range(N, total + 1):
    ways = math.comb(total, i)
    ans += ways * (p ** i) * ((1 - p) ** (total - i))

print(ans)
