'''
BFS
'''
from collections import deque

def icecream(i, j, graph):
    que = deque()
    que.append((i, j))
    visited = set()
    visited.add((i, j))
    graph[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            xx = dx[i]
            yy = dy[i]

            if x + xx < 0 or y + yy < 0 or x + xx >= N or y + yy >= M:
                continue

            if graph[x + xx][y + yy] == 0:
                graph[x + xx][y + yy] = 1
                que.append((x + xx, y + yy))

N, M = map(int, input().split())
graph = []
cnt = 0

for _ in range(N):
    S = input()
    graph.append(list(map(int, S)))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            icecream(i, j, graph)
            cnt += 1

print(cnt)

'''
[input]
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

[output]
8
'''
