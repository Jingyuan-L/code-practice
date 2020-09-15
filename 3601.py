while True:
    pwd = input().strip()
    score = [False] * 5
    if len(pwd) <= 8:
        print("Irregular password")
    else:
        score[4] = True
        for c in pwd:
            if c.isdigit():
                score[0] = True
            elif c.isupper():
                score[1] = True
            elif c.islower():
                score[2] = True
            elif 33 <= ord(c) <= 47 or 58 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123 <= ord(c) <= 126:
                # print(ord(c))
                score[3] = True
            if all(score):
                print("Ok")
                break
        # print(score)
        if not all(score):
            print("Irregular password")
