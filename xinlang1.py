def count(steps):
    dp = 2
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return  2
    for i in range(3,steps + 1):
        dp *= 2
    return dp

print(count(4))