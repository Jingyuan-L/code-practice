n = int(input().strip())
res = [[0] * n for _ in range(n)]
flag = True
mid = n//2
if n%2 == 0:
    flag = False
for i in range(n):
    for j in range(n):
        #两条中间的分割线
        if flag and (i == mid or j == mid):
            continue
        #两条 对角线
        if i == j or i == n - j -1:
            continue
        #各个区域内元素
        if i < mid:
            if j < mid:
                if i < j:
                    res[i][j] = 2
                else:
                    res[i][j] = 3
            else:
                if i < n - j -1:
                    res[i][j] = 1
                else:
                    res[i][j] = 8
        else:
            if j < mid:
                if i < n - j -1:
                    res[i][j] = 4
                else:
                    res[i][j] = 5
            else:
                if i < j:
                    res[i][j] = 7
                else:
                    res[i][j] = 6
    print(" ".join([str(res[i][j]) for j in range(n) ]))

