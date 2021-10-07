from itertools import combinations
from collections import deque
from collections import Counter
import copy
import sys

def bfs(graph):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j]==2:
                que.append((i,j))

    while que:
        x,y=que.popleft()

        for i in range(4):
            xx=dx[i]
            yy=dy[i]

            if x+xx<0 or y+yy<0 or x+xx>=N or y+yy>=M:
                continue

            if graph[x+xx][y+yy]==0:
                graph[x+xx][y+yy]=2
                que.append((x+xx,y+yy))


N,M=map(int,sys.stdin.readline().strip().split())
wall=[]
graph=[]
Max=0

for i in range(N):
    List=list(map(int,sys.stdin.readline().strip().split()))
    graph.append(List)
    for j in range(M):
        if List[j]==0:
            wall.append((i,j))

combination=list(combinations(wall,3))

#벽 세우기
for com in combination:
    temp_graph=copy.deepcopy(graph)
    for x,y in com:
        temp_graph[x][y]=1

    bfs(temp_graph)

    # 안전구역
    cnt=0
    for k in range(N):
        counter=Counter(temp_graph[k])
        cnt+=counter[0]

    if Max<cnt:
        Max=cnt

print(Max)

'''
[input]
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

[output]
27
'''