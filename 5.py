A, B, C, X, Y = map(int, input().split())

# 最安値を求めるので初期値は十分大きくしておく
price = 10 ** 10

# ループ回数は最大でもXかYの大きいほうの2倍
roop_count = 10 ** 5
if X > Y:
    roop_count = 2 * X
else:
    roop_count = 2 * Y

# ループを回す回数は、ピザABの購入個数で回す
for i in range(0, roop_count + 1):
    # 奇数は損しかしないのでスキップ
    if i % 2 == 1:
        continue

    # ABのピザをi個購入して、必要分AとBを買い足していく
    tmp_price = 0
    tmp_price += C * i
    if X - i//2 > 0:
        # Aのピザが不足している場合、Aを買い足す
        tmp_price += A * (X - i//2)
    if Y - i//2 > 0:
        # Bのピザが不足している場合、Bを買い足す
        tmp_price += B * (Y - i//2)
    # マイループごとに最小値を更新する
    price = min(tmp_price, price)

print(price)
