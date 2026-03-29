a = input("Enter your DNA string: ")
b = input("String that you want to find in a: ")
positions = []

for i in range(len(a)):
    # Check if substring of length len(b) starting at i matches b
    if a[i:i+len(b)] == b:
        positions.append(i + 1)  # +1 for 1-based position

print("Locations of b in a:", positions)


