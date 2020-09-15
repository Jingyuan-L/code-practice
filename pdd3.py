num, container = list(map(int, input().strip().split()))
details = [[0] * 2 for _ in range(num)]
for i in range(num):
    cur = list(map(int, input().strip().split()))
    details[i][0] = cur[0]
    details[i][1] = cur[1]

extra = sum(details[i][1] for i in range(num) if details[i][1] < 0)
extra = -extra if extra < 0 else 0
dp = [[0] * (container+1+extra) for _ in range(num+1)]
#对于物品数量的动态规划
for i in range(1, num+1):
    #对与背包容量的动态规划
    for j in range(1, container+1+extra):
        #第i个不选
        dp[i][j] = dp[i-1][j]
        #判断容量是不是大于第i个物品
        if j >= details[i-1][0]:
            #取装或不装的最大值
            dp[i][j] = max(dp[i][j], dp[i-1][j-details[i-1][0]] + details[i-1][1])
print(dp[-1][-1])
