import sys

args = sys.argv
N = int(args[1]) * -1

with open('hightemp.txt', 'r') as f:
    data = f.read()

lines = data.rstrip("\n").split("\n")
print("\n".join(lines[N:]))
