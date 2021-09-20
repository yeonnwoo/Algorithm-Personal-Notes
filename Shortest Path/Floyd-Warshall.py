'''every node -> every node'''

# 노드의 개수, 간선의 개수
n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 것은 0으로 초기화
for i in range(n + 1):
    graph[i][i] = 0

# 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

'''
거쳐가는 노드 K
min(i->j, i->k + k->j)
'''
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print('')
'''
[input]
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

[output]
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''
