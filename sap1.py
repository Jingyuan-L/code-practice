N = input('Enter a number: ')

N = int(N)

arr = []

for i in range(N):
    arr.append(i**2)

print('Squares up to ' + str(N) + ' are: ')

print(arr)