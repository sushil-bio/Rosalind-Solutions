a = input().upper()
s= str.maketrans("ATGC", "TACG")
print(a.translate(s)[::-1])