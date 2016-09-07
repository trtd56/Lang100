from Q20 import TEXT

for line in TEXT.split("\n"):
    if "Category" in line:
        print(line)
