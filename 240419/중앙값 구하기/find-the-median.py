a, b, c = map(int, input().split())

max_t = max(a, b, c)
min_t = min(a, b, c)

if a != max_t and a != min_t:
    print(a)
elif b != max_t and b != min_t:
    print(b)
else:
    print(c)