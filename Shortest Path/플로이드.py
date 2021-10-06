import sys

n = int(sys.stdin.readline().rstrip())  # 도시의 개수
m = int(sys.stdin.readline().rstrip())  # 버스의 개수

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for List in graph:
    print(*List)

'''
[input]
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

[output]
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
'''