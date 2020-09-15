nums = list(map(int, input().strip().split()))
groups = [[]] * nums[1]
for i in range(nums[1]):
    groups[i] = list(map(int, input().strip().split()))
start = 0
for i in range(nums[1]):
    if 0 in groups[i][1:]:
        start = i
        break

queue = set(groups[start][1:])
flag = [True] * nums[1]
flag[start] = False
for j in range(nums[1]):
    if flag[j]:
        for person in groups[j][1:]:
            if person in queue:
                new_set = set(groups[j][1:])
                queue |= new_set
                flag[j] = False
                # print( flag, queue)
print(len(queue))
