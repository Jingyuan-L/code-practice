grid = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

string = input().upper()
def dfs(used, index, x, y):
    if index >= len(string):
        return True
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    if not used[x][y] and grid[x][y] == string[index]:
        used[x][y] = True
        return dfs(used, index+1, x+1, y) or dfs(used, index+1, x-1, y) or dfs(used, index+1, x, y+1) or dfs(used, index+1, x, y-1)
    else:
        return False
res = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        used = [[False] * len(grid[0]) for _ in range(len(grid))]
        if grid[i][j] == string[0]:
            cur = dfs(used, 0, i, j)
            res.append(cur)
if any(res):
    print('true')
else:
    print('false')