def numSum(n):
    left = 1
    for right in range(n//2 + 1):
        res = []
        num_sum = sum([i for i in range(left, right + 1 )])
        if num_sum > n:
            left += 1
        elif num_sum == n:
            res.append([i for i in range(left, right + 1)])

numSum(5)


