total = 0
cnt = 0

while True:
    a = int(input())

    if a // 10 != 2:
        break
    
    total += a
    cnt += 1

avg = total / cnt

print(f"{avg:.2f}")