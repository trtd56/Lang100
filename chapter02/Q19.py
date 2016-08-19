with open('hightemp.txt', 'r') as f:
    data = f.read()

col1 =  [i.split("\t")[0] for i in data.rstrip("\n").split("\n")]
col1_set = set(col1)
count_dict = {i:col1.count(i) for i in col1_set}

arranged_list = sorted(count_dict,key=lambda x:x[1])
arranged_list.reverse()
print("\n".join(arranged_list))
