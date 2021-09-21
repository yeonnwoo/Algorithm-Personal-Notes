'''
n(i)=max(n(i-1),n(i-2)+now)
'''

n=int(input())
Foods=[0]+list(map(int,input().split()))

#지금까지 저장된 식량의 최대값
dp=[0]*(n+1)
dp[1]=Foods[1]
dp[2]=Foods[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-2]+Foods[i])

print(dp[n])

'''
[input]
4
1 3 1 5

[output]
8
'''