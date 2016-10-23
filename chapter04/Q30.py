# coding: utf-8
import MeCab

f = open('neko.txt')
text = f.readlines()
f.close()

text = "".join(text)

tagger = MeCab.Tagger("-Ochasen")
text_elem = tagger.parse(text)


mapping_list = []
for line in text_elem.split("\n"):
    elems = line.split("\t")
    if len(elems) == 6:
        sp_pos= elems[3].split("-")
        pos = sp_pos[0]
        if len(sp_pos) > 1:
            pos1 = sp_pos[1]
        else:
            pos1 = ""
        dic = {"surface":elems[0], "base":elems[2], "pos":pos, "pos1":pos1}
        mapping_list.append(dic)

#print mapping_list
