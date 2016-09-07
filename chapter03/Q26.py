import re
from Q20 import TEXT


def strong_filter(text):
    return re.sub("'{2,5}", "", text) 

dic = {}
for line in re.split("\n[\|}]", TEXT):
    grep_line = re.search("^(.*?)\s=\s(.*?)$",line)
    if grep_line is not None:
        text = strong_filter(grep_line.group(2))
        dic[grep_line.group(1)] = text

if __name__=="__main__":
    for k,v in dic.items():
        print(k,"->",v)
