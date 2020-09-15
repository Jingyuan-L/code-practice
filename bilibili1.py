def GetFragment(str):
    # write code here
    i= 0
    sumlen = 0
    num = 0
    while i < len(str):
        cur = str[i]
        while i < len(str) - 1 and str[i] == str[i + 1]:
            cur += str[i + 1]
            i += 1
        sumlen += len(cur)
        num += 1
        i += 1
        # print(cur, sumlen, num)
    return sumlen // num

print(GetFragment("aaabbaaac"))