n = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

total = 0
minn = float("inf")
mf, ms, mt = 0, 0, 0

for f in range(n-2):
    for s in range(f+1, n-1):
        for t in range(s+1, n):
            total = (num_lst[f] + num_lst[s] + num_lst[t])
            if minn > abs(total):
                minn = abs(total)
                mf, ms, mt = f, s, t

print(num_lst[mf], num_lst[ms], num_lst[mt])