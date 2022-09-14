N, M = map(int, input().split())

point_list = []

for i in range(N):
    point_list.append(list(map(int, input().split())))

########################

import itertools
T1_T2_list = list(itertools.permutations(range(M), 2))

ans = 0

for T1_T2 in T1_T2_list:
    score = 0
    T1 = T1_T2[0]
    T2 = T1_T2[1]

    for point in point_list:
        score += max(point[T1], point[T2])

    ans = max(score, ans)

print(ans)
