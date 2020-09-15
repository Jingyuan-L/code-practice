def GetMaxConsecutiveOnes(arr, k):
    # write code here
    i = 0
    #save the number of 1 and number of 0
    #index 0,2,4... represent 1
    nums = []
    #ignore the first several 0
    while arr[i] == 0:
        i += 1
    print(i)
    #start from the first 1 sequence
    while i < len(arr):
        cur = 1
        while i + 1 < len(arr) and arr[i] == arr[i+1]:
            cur += 1
            i += 1
        nums.append(cur)
        i += 1
    print(nums)
    res1 = max([nums[i] for i in range(0,len(nums), 2)]) + k
    print(res1)
    remain = k
    res2 = 0
    for j in range(1, len(nums), 2):
        if nums[j] <= remain:
            back = nums[j+1] if j+1 < len(nums) else 0
            res2 = max(res2, nums[j-1] + back)
            remain -= nums[j]

        else:
            res2 += remain
        if remain == 0:
            remain == k

    return max(res1, res2)

print(GetMaxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0], 2))


