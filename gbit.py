n = int(input().strip())
res = 1
for i in range(2, n+1):
    while n != i:
        if n%i == 0:
            res += 1
            n //= i
        else:
            break
print(str(res))