n = int(input())

cnt = 1

while True:
    n //= cnt
    if n <= 1:
        break
    cnt += 1

print(cnt)