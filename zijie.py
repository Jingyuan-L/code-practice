words = list(input().split())
word_dict = set(words)
s = input()
dp = [False] * (len(s)+1)
dp[0] = True
for i in range(len(s)+1):
    for j in range(i):
        if dp[j] and s[j:i] in word_dict:
            dp[i] = True
            break

print(dp[len(s)])
