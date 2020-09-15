import sys

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    res = []


    def helper(res, cur, numa, numb):
        print(res)
        if numa > nums[0] and numb > nums[1]:
            return
        if len(res) - 1 == nums[2]:
            # print(res[-1])
            return
        res.append(cur)
        if numa < nums[0]:
            helper(res, cur + "a", numa + 1, numb)
        if numb < nums[1]:
            helper(res, cur + "b", numa, numb + 1)


    helper(res, "", 0, 0)
    print(res[nums[2]])
