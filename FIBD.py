n, m = map(int, input().split())

# rabbits[i] = number of rabbit pairs of age i
rabbits = [0] * m
rabbits[0] = 1  # month 1: one newborn pair

for month in range(1, n):
    newborns = sum(rabbits[1:])   # all mature rabbits reproduce
    rabbits = [newborns] + rabbits[:-1]  # age shift (oldest die)

print(sum(rabbits))
