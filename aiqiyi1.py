s = input().strip()
char_set = set()
length = 0
i, j = 0, 0
while i < len(s) and j < len(s):
    if s[j] not in char_set:
        char_set.add(s[j])
        j += 1
        length = max(length, j - i)
    else:
        char_set.remove(s[i])
        i += 1

print(length)