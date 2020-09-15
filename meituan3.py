n = int(input().strip())
nums = list(map(int, input().strip().split()))
res = 0
for i in range(1, n+1):
    res ^= nums[i-1]
    for j in range(1, n+1):
        if i <= j:
            res ^= i
        else:
            res ^= i % j
print(res)