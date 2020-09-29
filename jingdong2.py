num = int(input().strip())
for _ in range(num):
    [n, m] = list(map(int, input().strip().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(input().strip()))
    # print(matrix)
    # find the positions of prince and princess
    prince = None
    princess = None
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                prince = [i, j]
            elif matrix[i][j] == 'E':
                princess = [i, j]
    # print(prince, princess)
    visited = [[False] * m for _ in range(n)]
    visited[prince[0]][prince[1]] = True
    # print(visited)
    def dfs(i, j):
        # print(i, j, matrix[i][j])
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        visited[i][j] = True
        if matrix[i][j] == '#':
            return False
        if matrix[i][j] == 'E':
            return True

        for new_i, new_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and dfs(new_i, new_j):
                return True

        return False
    # print(visited)
    if dfs(prince[0], prince[1]):
        print('YES')
    else:
        print('NO')