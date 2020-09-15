
n = int(input())
nums = list(map(int, input().strip().split()))
sorted_nums = sorted(nums)
mid = n//2 - 1
for i in range(n):
    if nums[i] <= sorted_nums[mid]:
        print(sorted_nums[mid+1])
    else:
        print(sorted_nums[mid])
