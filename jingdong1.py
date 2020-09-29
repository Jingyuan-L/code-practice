[n, p] = list(map(int, input().strip().split()))
stuff = []
for _ in range(n):
    stuff.append(list(map(int, input().strip().split())))
stuff.sort(key= lambda x: -x[2]/x[1])
# print(stuff)
res = 0
for i in range(n):
    if p - stuff[i][1] >= 0:
        num = p//stuff[i][1] if p//stuff[i][1] <= stuff[i][0] else stuff[i][0] # the most numbers he can buy
        p -= num * stuff[i][1]  # total cost
        res += num * stuff[i][2] #total charm value
    if p <= 0:
        break
print(res)