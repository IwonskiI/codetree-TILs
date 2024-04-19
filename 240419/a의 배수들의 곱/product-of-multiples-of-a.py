a, b = map(int, input().split())

total = 1

for i in range(1, b+1):
    if i % a == 0:
        total *= i

print(total)