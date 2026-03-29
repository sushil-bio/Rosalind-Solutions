# a: total months, b: offspring per litter
a, b = map(int, input().split())

# Create a list to store the population for each month
F = [0] * (a + 1)

# Base cases: Month 1 and 2 start with 1 pair
F[1] = F[2] = 1

# Recurrence: Total = (Previous Month) + (Offspring * Parents from 2 months ago)
for i in range(3, a + 1):
    F[i] = F[i - 1] + (b * F[i - 2])

# Output the population at the final month
print(F[a])