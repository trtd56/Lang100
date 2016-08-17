def cipher(words):
    print("".join([str(219-ord(i)) if i.islower() else i for i in words]))

cipher("HogeFugaPiyo")
