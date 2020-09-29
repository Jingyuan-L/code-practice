m = int(input().strip())
n = int(input().strip())
a, b, c = 1, 1, 1
for i in range(2, m+1):
    a *= i
for i in range(2, n+1):
    b *= i
for i in range(2, m-n+1):
    c *= i
print(str(a//(b*c)))