[n, m] = list(map(int, input().strip().split()))
records = []
edges = {}
for _ in range(n):
    records.append(list(map(int, input().strip().split())))
print(records)
for _ in range(m):
    cur = list(map(int, input().strip().split()))
    if not edges.get(cur[0]):
        edges[cur[0]] = []
    edges[cur[0]].append(cur[1])
print(edges)
records.sort(key= lambda x: (x[1], x[0]))
print(records)
state_index = {1:0}
for i in range(1, n):
    if records[i][1] == records[i-1][1]:
        continue
    state_index[records[i][1]] = i
print(state_index)
def dfs(cur_state, res, index, pre_time):

    print(cur_state, res, index, pre_time)
    while index < n and records[index][1] == cur_state:
        if index < n and records[index][0] < pre_time:
            index += 1
            print("index+ +", index, records[index][0], pre_time)
            continue
        res += 1
        pre_time = records[index][0]
        index += 1
    print(res, index, pre_time)

    if not edges.get(cur_state):
        print(cur_state, res)
        return res

    new_res = []
    for nxt_state in edges[cur_state]:
        new_res.append(dfs(nxt_state, res, state_index[nxt_state], pre_time))
    print(new_res)
    return max(new_res)

print(dfs(1, 0, 0, 0))