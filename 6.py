N = int(input())
S = input()

count = 0

# 答えの候補になる "000" ~ "999"の内いくつが実現可能かカウントする
for i in range(1000):
    # 0パディングで3桁
    num = str(i).zfill(3)
    # 候補値の100のくらいの値でS内のインデックスを求める
    n1 = S.find(num[0])
    # Sの不要部分を切り落とした中から候補値の10のくらいの値のインデックスを求める
    n2 = S[n1+1:N].find(num[1])
    # Sの不要部分をさらに切り落とした中から候補地の1のくらいの値のインデックスを求める
    n3 = S[n1+n2+2:N].find(num[2])

    if n1 != -1 and n2 != -1 and n3 != -1:
        count += 1
        # print(num)

print(count)
