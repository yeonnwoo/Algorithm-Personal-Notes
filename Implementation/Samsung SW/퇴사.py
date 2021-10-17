N=int(input())
List=[(0,0)]
dp=[0]*(N+1)

for _ in range(N):
    a,b=map(int,input().split())
    List.append((a,b))

for i in range(N,0,-1):
    if i+List[i][0] > N+1:
        if i==N:
            continue
        else:
            dp[i]=dp[i+1]

    else:
        if i==N:
            dp[i]=List[i][1]
        else:
            if i+List[i][0]==N+1:
                dp[i]=max(List[i][1],dp[i+1])
            else:
                dp[i]=max(List[i][1]+dp[i+List[i][0]],dp[i+1])

print(dp[1])