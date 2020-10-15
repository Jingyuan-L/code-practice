
def is_valid(matrix, i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
        return True

    return False

def max_height(matrix):
    next_pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = []
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                for neighbor in next_pos:
                    if is_valid(matrix, i+neighbor[0], j+neighbor[1]):
                        queue.append([i+neighbor[0], j+neighbor[1], 1])
                        visited[i+neighbor[0]][j+neighbor[1]] = True

    while queue:
        [i, j, layer] = queue.pop(0)
        matrix[i][j] = layer
        for neighbor in next_pos:
            if is_valid(matrix, i + neighbor[0], j + neighbor[1]) and not visited[i+neighbor[0]][j+neighbor[1]]:
                queue.append([i + neighbor[0], j + neighbor[1], layer+1])
                visited[i + neighbor[0]][j + neighbor[1]] = True
    m_list = []
    for row in matrix:
        m_list.extend(row)
    return max(m_list)


matrix = [
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1]
]
'''[
    [0, 0, 1, 1, 1, 0],
    [0, 1, 2, 2, 2, 1],
    [1, 1, 2, 1, 2, 1],
    [0, 0, 1, 2, 1, 0],
    [0, 1, 2, 2, 1, 0],
    [0, 0, 1, 1, 0, 1]
    ]
    [
    [0, 0, 1, 1, 1, 0],
    [0, 1, 2, 2, 2, 1],
    [1, 1, 2, 3, 2, 1],
    [0, 0, 1, 2, 1, 0],
    [0, 1, 2, 2, 1, 0],
    [0, 0, 1, 1, 0, 1]
    ]
    ]
'''
res = max_height(matrix)
print(res)
