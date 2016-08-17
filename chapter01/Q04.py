Text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
Indexs = [1, 5, 6, 7, 8, 9, 15, 16, 19]


word_list = Text.replace(".", "").split()
is_contained = map(lambda x: x+1 in Indexs , range(len(word_list)))

sp_word_list = [word[0] if permit else word[:2] for word, permit in zip(word_list, is_contained)]

print({w:i for i, w in enumerate(sp_word_list)})
