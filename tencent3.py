from collections import Counter
nums = list(map(int, input().strip().split()))
strings = []
for i in range(nums[0]):
    strings.append(input().strip())
# print(strings)
counter = Counter(strings)
common = counter.most_common(nums[1])
for i in range(nums[1]):
    print(common[i][0], common[i][1])
uncommon = sorted(counter.items(), key=lambda x: x[1])
for i in range(nums[1]):
    print(uncommon[i][0], uncommon[i][1])
