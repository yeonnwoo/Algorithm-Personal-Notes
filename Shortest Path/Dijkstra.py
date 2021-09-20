'''1 node -> every node'''
import heapq

INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

# 그래프
graph = [[] for _ in range(n + 1)]

# 최단거리
distance = [INF] * (n + 1)
distance[start] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b로 가는 비용이 c

heap = []
heapq.heappush(heap, (0, start))  # 가중치, 노드

while heap:
    cost, node = heapq.heappop(heap)

    if distance[node] < cost:
        continue

    for temp_node, temp_cost in graph[node]:
        new_cost = cost + temp_cost

        if new_cost < distance[temp_node]:
            distance[temp_node] = new_cost
            heapq.heappush(heap, (new_cost, temp_node))

for i in range(1, len(distance)):
    print(distance[i])

'''
O(E*logV)
[input]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

[output]
0
2
3
1
2
4
'''
