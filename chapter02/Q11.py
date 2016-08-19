with open('hightemp.txt', 'r') as f:
    data = f.read()

print(data.rstrip("\n").replace("\t"," "))
