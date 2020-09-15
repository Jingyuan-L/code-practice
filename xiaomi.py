passwords = list(input().strip().split())
for password in passwords:
    if len(password) < 8 or len(password) > 120:
        print(1)
    else:
        type = [False] * 4
        for c in password:
            if c.isdigit():
                type[0] = True
            elif 33 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123<= ord(c) <= 126:
                type[1] = True
            elif c.isupper():
                type[2] = True
            elif c.islower():
                type[3] = True
            if all(type):
                break
        if all(type):
            print(0)
        else:
            print(2)