t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    stuff = [[] for _ in range(n)]
    # print(stuff)
    x = list(map(int, input().strip().split()))
    y = list(map(int, input().strip().split()))
    for i in range(n):
        stuff[i].append(x[i])
        stuff[i].append(y[i])
    # print(stuff)
    stuff.sort(key= lambda x: (x[0], x[1]))
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(2, i+1):
            print(i, j)
            if stuff[j-1][0] > stuff[j-2][0] and stuff[j-1][1] > stuff[j-2][1]:
                print(stuff[j-1][0], stuff[j-2][0], stuff[j-1][1], stuff[j-2][1])
                dp[i] = max(dp[i], dp[i-1]+1)
                print(dp)
        else:
            continue
    print(dp[-1])
