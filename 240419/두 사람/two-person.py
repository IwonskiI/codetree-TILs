f_a, f_s = input().split()
s_a, s_s = input().split()

if (int(f_a) >= 19 and f_s == "M") or (int(s_a) >= 19 and s_s == "M"):
    print(1)
else:
    print(0)