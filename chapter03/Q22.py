import re
from Q20 import TEXT

for line in TEXT.split("\n"):
    if "Category" in line:
        grep_line = re.search("^\[\[Category:(.*?)(\|.*)*\]\]$",line)
        print(grep_line.group(1))

