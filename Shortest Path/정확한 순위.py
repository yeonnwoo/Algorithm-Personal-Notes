N,M=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(N+1) for _ in range(N+1)]
result=0

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=-1
    graph[b][a]=-1

for k in range(1,N):
    for i in range(1,N):
        for j in range(1,N):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

for i in range(1,N):
    List=graph[i]
    cnt=len([j for j in List if j==INF])
    if cnt==1:
        result+=1


print(result)

'''
[input]
6 6
1 5
3 4
4 2
4 6
5 2
5 4

[output]
1
'''