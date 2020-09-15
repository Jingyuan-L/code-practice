n, m = list(map(int, input().strip().split()))
y = []
for i in range(m):
    cur = int(input().strip())
    if cur == 1:
        print(n)
        exit(0)
    y.append(cur)

res = [0] * n
#对每个数字n判断是否被特征值整除
for i in range(n):
    #如果当前数字是前面已经判断过的数字的倍数
    #并且前面那个数字是“特征显著”
    #则当前数字也特征显著
    for j in range(1, (i)//2):
        if res[j] == 1 and (i+1)%(j+1) == 0:
            res[i] = 1
            break

    if res[i] == 1:
        continue
    else:
        for yi in y:
            if (i+1) % yi == 0:
                res[i] = 1
                break
print(sum(res))

