while True:
    n = int(input())
    if n is None:
        break
    nums = list(map(int, input().strip().split()))
    numsset = set(nums)
    root = max(nums)
    if 2 in numsset or root > n:
        print("NO")
    else:
        numofone = 0
        sumofdegree = 0
        for num in nums:
            sumofdegree += num - 1
            if num == 1:
                numofone += 1
        if numofone + 1 != root or sumofdegree != n:
            print("NO")
        else:
            print("YES")