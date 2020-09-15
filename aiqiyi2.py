nums = list(map(int, input().strip().split()))
count = {}
for i in range(len(nums)):
    if count.get(nums[i]):
        count[nums[i]] += 1
    else:
        count[nums[i]] = 1
print(max(count.keys(), key=count.get))
