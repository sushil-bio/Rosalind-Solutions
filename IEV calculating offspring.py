a = input()
b = {}

for word in a.lower().split():
    b[word] = b.get(word, 0) + 1

print(b)
