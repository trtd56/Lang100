with open('hightemp.txt', 'r') as f:
    data = f.read()

print(len(data.rstrip("\n").split("\n")))
