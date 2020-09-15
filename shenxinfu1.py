
def lastRemaining(n , m ):
        # write code here
    nums = [i for i in range(n)]
    pre_index = -1
    while len(nums) > 1:
        index = (pre_index + m) % len(nums)
        pre_index = index - 1
        nums.remove(nums[index])
        print(nums)

    return nums[0]

print(lastRemaining(7, 3))