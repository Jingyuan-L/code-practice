def order(marix):
    res = []
    if not marix:
        return []
    l = 0
    r = len(marix[0]) - 1
    u = 0
    d = len(marix) - 1
    while l <= r and u <= d:
        #right
        for i in range(l, r+1):
            res.append(marix[l][i])
        u += 1
        #down
        for i in range(u, d+1):
            res.append(marix[i][r])
        r -= 1
        if u <= d:
            #left
            for i in range(r, l-1, -1):
                res.append(marix[d][i])
            d -= 1
        if l <= r:
            #up
            for i in range(d, u-1, -1):
                res.append(marix[i][l])
            l += 1
    return res

print(order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
