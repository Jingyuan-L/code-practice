
def compileSeq(inputs):
    nums = list(map(int, inputs.split(",")))
    dict = {}
    exists = set()
    res = []
    is_possible = True
    for i in range(len(nums)):
        if nums[i] == -1:
            break
        if not nums[i] in exists:
            dict[i] = []
            exists.add(i)
        dict[i].append(nums[i])
    states = {k: 0 for k in range(len(nums))}
    def dfs(n):
        nonlocal is_possible
        if not is_possible:
            return
        states[n] = 1
        if n in dict:
            for nxt in dict[n]:
                if states[nxt] == 0:
                    dfs(nxt)
                elif states[nxt] == 1:
                    is_possible = False
        states[n] = 2
        res.append(n)
    for n in range(len(nums)):
        if states[n] == 0:
            dfs(n)
    return ",".join(map(str, res)) if is_possible else "false"

res = compileSeq("1,2,-1,1")
print(res)