from Q05 import char_n_gram

Text1 = "paraparaparadise"
Text2 = "paragraph"

X = set(char_n_gram(Text1,2))
Y = set(char_n_gram(Text2,2))

wa = X | Y
seki = X & Y
sa = X - Y

print("X:",X)
print("Y:",Y)
print("和:",wa)
print("積:",seki)
print("差:",sa)

if ("s", "e") in X:
    print("se in X")
if ("s", "e") in Y:
    print("se in Y")
