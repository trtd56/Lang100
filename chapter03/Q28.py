import re
from Q20 import TEXT
from Q26 import strong_filter
from Q27 import link_filter

def markdown_filter(text):
    text = strong_filter(text)
    text = link_filter(text)
    text = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", text)
    text = re.sub(r"<.*?>", r"", text)
    return re.sub(r"\[.*?\]", r"", text)

dic = {}
for line in re.split("\n[\|}]", TEXT):
    grep_line = re.search("^(.*?)\s=\s(.*?)$",line)
    if grep_line is not None:
        text = markdown_filter(grep_line.group(2))
        dic[grep_line.group(1)] = text

Dic = dic

if __name__=="__main__":
    for k,v in dic.items():
        print(k,"->",v)
