'''Topology Sort => O(V+E)'''
from collections import deque

result = []

# 노드의 개수,간선의 개수
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

# 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 진입차수 0인 노드 que에 삽입
que = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    p = que.popleft()
    result.append(p)

    # 간선 제거
    for node in graph[p]:
        indegree[node] -= 1

        if indegree[node] == 0:
            que.append(node)

print(*result)

'''
[input]
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

[output]
1 2 5 3 6 4 7
'''
