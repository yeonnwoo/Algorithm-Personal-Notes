'''
Bottom-up

dp[i]=min(dp[i-1],dp[i//2],dp[i//3],dp[i//5])+1
'''

n = int(input())

# 연산의 횟수 저장
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[n])

'''
[input]
26

[output]
3
'''
