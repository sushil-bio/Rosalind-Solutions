DNA1 = input().strip()

DNA2 = input().strip()

count = 0

for DNA in range(len(DNA1)):
    if DNA1[DNA] != DNA2[DNA]:
     count += 1
print(count)