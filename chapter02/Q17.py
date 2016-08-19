with open('hightemp.txt', 'r') as f:
    data = f.read()

col1 = [i.split("\t")[0] for i in data.rstrip("\n").split("\n")]
print("\n".join(list(set(col1))))
