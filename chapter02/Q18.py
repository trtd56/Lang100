with open('hightemp.txt', 'r') as f:
    data = f.read()

lines =  data.rstrip("\n").split("\n")

col3 = {i:float(v) for i,v in enumerate([i.split("\t")[2] for i in lines])}
index = sorted(col3)
index.reverse()

print("\n".join([lines[i] for i in index]))
