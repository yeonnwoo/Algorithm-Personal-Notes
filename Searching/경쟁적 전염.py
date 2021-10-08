import sys
from collections import deque

# N*N 시험관,1~K 바이러스
N, K = map(int, sys.stdin.readline().strip().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

# S초가 지난후 X,Y
S, X, Y = map(int, sys.stdin.readline().strip().split())

que = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            que.append((graph[i][j], 0, i, j))  # 바이러스,시간,x,y좌표

que.sort()
que=deque(que)

while que:
    virus,Time,x, y = que.popleft()

    if Time==S:
        break

    for i in range(4):
        xx = dx[i]
        yy = dy[i]

        if x + xx < 0 or y + yy < 0 or x + xx >= N or y + yy >= N:
            continue

        if graph[x+xx][y+yy]==0:
            graph[x + xx][y + yy] = virus
            que.append((virus,Time+1,x+xx,y+yy))

print(graph[X - 1][Y - 1])

'''
[input]
3 3
1 0 2
0 0 0
3 0 0
2 3 2

[output]
3
'''
