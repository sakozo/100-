S = input()
S_list = list(S)

len_list = [0]

count = 0

for s in S_list:
    if s in ["A","C","G","T"]:
        count += 1
    else:
        len_list.append(count)
        count = 0

# ループの中で一度もelseに入らないパターンの場合の時Listに追加するタイミング
len_list.append(count)

print(max(len_list))