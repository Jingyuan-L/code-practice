[n, m] = list(map(int, input().strip().split()))
edges = {}
for i in range(m):
    cur = list(map(int, input().strip().split()))
    if not edges.get(cur[0]) or not edges.get(cur[1]):
        if not edges.get(cur[0]):
            edges[cur[0]] = []
        if not edges.get(cur[1]):
            edges[cur[1]] = []
        edges[cur[0]].append([cur[1], cur[2]])
        edges[cur[1]].append([cur[0], cur[2]])
    else:
        edges[cur[0]].append([cur[1], cur[2]])
        edges[cur[1]].append([cur[0], cur[2]])
# print(edges)
[s, e, start] = list(input().strip().split())
s = int(s)
e = int(e)
# print(s, e, start)
open = []
open.append(s)
close = []
paths = []
while open:
    time = 0
    for nxt in edges[open[0]]:
        if nxt[0] == e:

        open.append(nxt[0])

