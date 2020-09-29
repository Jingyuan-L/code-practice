num = int(input().strip())
price = []
price.append(list(map(str, input().strip().split())))
price.append(list(map(str, input().strip().split())))
# print(price)
dp = [[0] * (num+1) for _ in range(num+1)]
# print(dp)
for i in reversed(range(num)):
    for j in reversed(range(num)):
        if price[1][i] == price[0][j]:
            dp[i][j] = dp[i+1][j+1] + 1
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j+1])
print(dp[0][0])
