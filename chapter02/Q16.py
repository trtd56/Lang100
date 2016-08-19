import sys

args = sys.argv
N = int(args[1])

with open('hightemp.txt', 'r') as f:
    data = f.read()

lines = data.rstrip("\n").split("\n")

div_len = int(len(lines)/N)
for i in range(div_len):
    div_line = "\n".join(lines[i*N:(i+1)*N])
    with open('div_'+str(i+1)+'.txt', 'w') as f:
        f.write(div_line)
