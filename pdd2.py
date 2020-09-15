n, m = list(map(int, input().strip().split()))
nums = []
for i in range(n):
    nums.append(list(map(int, input().strip().split())))

def move(x, y):
    res = set()
    for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
        if 0 <= x+i < n and 0 <= y+j < n:
            res.add((x+i, y+j))
    return res

def dfs(x, y, index):
    res = 0
    nums[x][y] = index
    for i, j in move(x, y):
        if nums[i][j] == 1:
            res += dfs(i, j, index)
    return res + 1

#深度遍历每个士兵集群并标号
index = 2
size = {0:0}
for x in range(n):
    for y in range(n):
        if nums[x][y] == 1:
            size[index] = dfs(x, y, index)
            index += 1
#遍历每一个为0的位置，计算合并后的区域大小
res = max(size.values())
for x in range(n):
    for y in range(n):
        if nums[x][y] == 0:
            add_index = set(nums[i][j] for i, j in move(x, y))
            res = max(res, sum(size[index] for index in add_index)+1)

print(res)