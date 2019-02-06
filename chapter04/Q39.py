import MeCab
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

tagger = MeCab.Tagger("-Ochasen")

words_dict = {}

with open('neko.txt', 'r') as f:
    most_long = ''
    for line in f:
        line = line.replace('\n', '')
        text_elem = tagger.parse(line)
        words_info = text_elem.split('\n')
        words_info = [w for w in words_info if w not in ['EOS', '']]
        for w_info in words_info:
            word, _, _, _, _, _ = w_info.split('\t')
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1

counts = []
for k, v in sorted(words_dict.items(), key=lambda x: -x[1]):
    counts.append(v)

c_dic = {}
for c in counts:
    if c not in c_dic.keys():
        c_dic[c] = 1
    else:
        c_dic[c] += 1

fig = plt.figure()
plt.scatter(c_dic.keys(), c_dic.values())
plt.xscale('log')
plt.yscale('log')
plt.savefig('Q39.png')
