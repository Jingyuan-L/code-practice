s = list(input().strip())
# print(s)
l, r = 0, len(s) - 1
while l < r:
    if s[l].isalpha() and s[r].isalpha():
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    while not s[l].isalpha():
        l += 1
    while not s[r].isalpha():
        r -= 1
print("".join(s))