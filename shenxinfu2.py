def make_cancellation(content, bomb):
    # write code here
    chars = list(content)
    i = 0
    while i < len(chars):
        # print(chars)
        while i >= 0 and i+1 < len(chars) and chars[i] == chars[i+1]:
            val = chars[i]
            del chars[i+1], chars[i]
            if val == bomb:
                if i-1 >= 0:
                    del chars[i-1]
                if i < len(chars):
                    del chars[i]
            i -= 1
        i += 1
    print(chars)
    return "".join(chars)

res = make_cancellation("112", "2")
print(res)