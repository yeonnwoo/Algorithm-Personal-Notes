'''
BFS
'''
from collections import deque

def BFS(graph):
    que=deque()
    que.append((0,0))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while que:
        x,y=que.popleft()

        for i in range(4):
            xx=dx[i]
            yy=dy[i]

            if x+xx<0 or y+yy<0 or x+xx>=N or y+yy>=M:
                continue

            if graph[x+xx][y+yy]==1:
                graph[x+xx][y+yy]=graph[x][y]+1
                que.append((x+xx,y+yy))

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    S=input()
    graph.append(list(map(int,S)))

BFS(graph)
print(graph[N-1][M-1])

'''
[input]
5 6
101010
111111
000001
111111
111111
'''