#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# M包糖果，抛M次硬币，硬币连续n次为正面，最多能得到多少颗糖果
# @param candies int整型一维数组 每包糖果的数量
# @param coin int整型一维数组 抛硬币的结果
# @param n int整型 连续是正面的次数
# @return int整型
#

def maxCandies(candies , coin , n ):
        # write code here
    max_n = sum(candies[0:n])
    magic_index = 0
    res = 0
    for i in range(1, len(candies)-n):
        cur = sum(candies[i:i+n])
        if cur > max_n:
            max_n = cur
            magic_index = i
    for i in range(len(candies)):
        if magic_index <= i < magic_index+n:
            coin[i] = 0
        if coin[i] == 0:
            res += candies[i]
    return res

res = maxCandies([3,5,7,2,8,8,15,3],[1,0,1,0,1,0,1,0],3)
print(res)