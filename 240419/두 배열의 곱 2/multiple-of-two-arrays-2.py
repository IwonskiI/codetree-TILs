a_lst = [list(map(int, input().split())) for _ in range(4)]
empty = input()
b_lst = [list(map(int, input().split())) for _ in range(4)]
total = [[0 for _ in range(2)] for _ in range(4)]

for c in range(4):
    for r in range(2):
        total[c][r] = a_lst[c][r] * b_lst[c][r]

for col in total:
    for row in col:
        print(row, end=" ")
    print()