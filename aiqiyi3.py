nums = list(map(int, input().strip().split()))
nums.sort()
res = []
for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    start, end = i+1, len(nums)-1
    while start < end:
        sum3 = nums[i] + nums[start] + nums[end]
        if sum3 < 0:
            start += 1
        elif sum3 > 0:
            end -= 1
        else:
            res.append([nums[i], nums[start], nums[end]])
            while start < end and nums[start] == nums[start+1]:
                start += 1
            while start < end and nums[end] == nums[end-1]:
                end -= 1
            start += 1
            end -= 1
for j in res:
    print(j[0], j[1], j[2])