n = int(input().strip())
string = input().strip()
res = ""
index = 0
while index < len(string):
    if index == 0:
        res += string[index+n-1::-1]
    else:
        res += string[index+n-1:index-1:-1]
    index += n
    # print(res,index)
res += string[len(string)-1:index-1:-1]
print(res)