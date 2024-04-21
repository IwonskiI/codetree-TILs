N = int(input())

aff_d = dict()
pos_lst = []

for _ in range(N):
    pos, aff = map(int, input().split())

    pos_lst.append(pos)
    aff_d[pos] = aff

pos_lst.sort()

prev = None
dist_lst = []
max_R = 1
next_flag = False

for p in pos_lst:
    if prev is None:
        if not aff_d.get(p):
            next_flag = True
    else:
        dist = p - prev
        dist_lst.append(dist)
        if next_flag:
            next_flag = False
            if max_R == 1:
                max_R = dist
            max_R = min(max_R, dist)
        if not aff_d.get(p):
            next_flag = True
            if max_R == 1:
                max_R = dist
            max_R = min(max_R, dist)
    prev = p

max_R -= 1
af_cnt = 1
min_d = float("inf")
cur_range = [-1, -1]
for i in range(N):
    if not aff_d.get(pos_lst[i]):
        continue
    if i == 0:
        min_d = pos_lst[i]
        cur_range = [pos_lst[i] - max_R, pos_lst[i] + max_R]
    else:
        in_range1 = pos_lst[i] - max_R <= min_d <= pos_lst[i] + max_R
        in_range2 = cur_range[0] <= pos_lst[i] <= cur_range[1]
        if in_range1:
            cur_range = [pos_lst[i] - max_R, pos_lst[i] + max_R]
        elif in_range2:
            continue
        else:
            cur_range = [pos_lst[i] - max_R, pos_lst[i] + max_R]
            af_cnt += 1

print(af_cnt)