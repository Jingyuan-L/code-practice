s = input().strip()
upper = 0
for c in s:
    if 65 <= ord(c) <= 90:
        upper += 1
lower = len(s) - upper
print(abs((upper - lower) // 2))