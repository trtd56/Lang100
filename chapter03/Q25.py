import re
from Q20 import TEXT


dic = {}
for line in re.split("\n[\|}]", TEXT):
    grep_line = re.search("^(.*?)\s=\s(.*?)$",line)
    if grep_line is not None:
        dic[grep_line.group(1)] = grep_line.group(2)

if __name__=="__main__":
    for k,v in dic.items():
        print(k,"->",v)
