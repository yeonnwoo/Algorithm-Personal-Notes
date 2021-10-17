T=int(input())

for _ in range(T):
    n,m=map(int,input().split())
    graph = []
    dp=[[0]*m for _ in range(n)]
    List=list(map(int,input().split()))
    dx=[0,-1,1] # 왼쪽,왼쪽위,왼쪽 아래
    dy=[-1,-1,-1]

    for i in range(0,n*m,m):
        graph.append(List[i:i+m])

    for i in range(n):
        for j in range(1,m):
            for k in range(3):
                x=dx[k]
                y=dy[k]

                if i+x<0 or j+y<0 or i+x>=n or j+y>=m:
                    continue



'''
[input]
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

[output]
19
16
'''