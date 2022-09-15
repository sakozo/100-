N = int(input())
A_list = []
B_list = []
for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

A_list.sort()
B_list.sort()

am = A_list[N//2]
bm = B_list[N//2]

ans = 0

for a,b in zip(A_list, B_list):
    ans += abs(a-b)
    ans += abs(a-am)
    ans += abs(b-bm)

print(ans)

