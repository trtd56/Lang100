# coding: utf-8
import MeCab

f = open('neko.txt')
text = f.readlines()
f.close()

text = "".join(text)

tagger = MeCab.Tagger("-Ochasen")
text_elem = tagger.parse(text)

dic = {}
