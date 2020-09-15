nums = list(map(int, input().strip().split()))
records = []
# details[0] stands for attend records, details[1] stands for leave records
details = [[False] * nums[0] for _ in range(2)]
for i in range(nums[1]):
    records.append(list(map(int, input().strip().split())))
    if records[i][1] == 1:
        details[0][records[i][0]-1] = True
    elif records[i][1] == 0:
        details[1][records[i][0]-1] = True
# print(records)
# print(details)
res = []
for i in range(len(details[0])):
    # if i == 0:
    #     print(i)
    #     res.append(i+1)
    # if i == nums[0] - 1:
    #     print(i)
    #     res.append(i+1)
    if details[0][i] is False and details[1][i] is False:
        # print(i)
        res.append(i+1)
if records[0][0] == records[-1][0]:
    res.append(records[1][0])
print(sorted(res))
