N = int(input())

temp_lst = []

for _ in range(N):
    a = int(input())
    if a % 3 == 0 and a % 2 != 0:
        temp_lst.append(a)

for num in temp_lst:
    print(num)