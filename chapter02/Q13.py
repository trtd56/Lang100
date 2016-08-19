with open('col1.txt', 'r') as f:
    data1 = f.read().rstrip("\n").split("\n")

with open('col2.txt', 'r') as f:
    data2 = f.read().rstrip("\n").split("\n")

print("\n".join([i+"\t"+j for i,j in zip(data1, data2)]))
