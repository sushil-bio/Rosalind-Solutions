text = ""
print("Enter text (press Enter on empty line to stop):")

while True:
    line = input()
    if line == "":
        break
    text += line + "\n"

for line_no, line in enumerate(text.splitlines(), start=1):
    if line_no % 2 == 0:
        print(line)
