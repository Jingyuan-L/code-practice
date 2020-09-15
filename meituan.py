nums = list(map(int, input().strip().split()))
a = set(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
both, onlyb = 0, 0
for i in b:
    if i in a:
        both += 1
    else:
        onlyb += 1
onlya = nums[1] - both
print(onlya, onlyb, both)
