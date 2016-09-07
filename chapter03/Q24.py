import re
from Q20 import TEXT

for line in TEXT.split("\n"):
    grep_line = re.search("(File:)(.*?)\|",line)
    if grep_line is not None:
        print(grep_line.group(2))

