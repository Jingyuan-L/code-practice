import sys
nums = list(map(int, input().strip().split()))
# print(nums)
#nums[0]物品数量 nums[1]物品重量 nums[2]预算

#details[i]中0,1,2分别表示价格，重量， 心动值
details = [[0] * 3 for _ in range(nums[0])]
# print(details)

for i in range(nums[0]):
    cur = list(map(int, input().strip().split()))
    # print(i, cur)
    for j in range(3):
        details[i][j] = cur[j]

#按照 心动值大色优先，价格便宜的优先，重量低的优先 排序
details.sort(key=lambda x: (-x[2], x[0], x[1]))
# print(details)
res, cost, weight = 0, 0, 0
#遍历每一件物品
for i in details:
    if cost + i[0] <= nums[2] and weight + i[1] <= nums[1]:
        res += 1
        cost += i[0]
        weight += i[1]
    else:
        break
sys.stdout.write(str(res))

