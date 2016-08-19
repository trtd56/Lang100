with open('hightemp.txt', 'r') as f:
    data = f.read()

lines = data.rstrip("\n").split("\n")

col1 = [l.split("\t")[0] for l in lines]
with open('col1.txt', 'w') as f:
    data = f.write("\n".join(col1))

col2 = [l.split("\t")[1] for l in lines]
with open('col2.txt', 'w') as f:
    data = f.write("\n".join(col2))
