'''Dij'''
import heapq

INF = int(1e9)
cnt = 0
result = 0

# 도시의 개수, 통로의 개수, 메시지 보내는 도시 C
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
distance[C] = 0

heap = []
heapq.heappush(heap, (0, C))

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

while heap:
    cost, node = heapq.heappop(heap)

    if distance[node] < cost:
        continue

    for temp_cost, temp_node in graph[node]:
        new_cost = temp_cost + cost

        if new_cost < distance[temp_node]:
            distance[temp_node] = new_cost
            heapq.heappush(heap, (new_cost, temp_node))

for i in range(1, N + 1):
    if distance[i] < INF:
        cnt += 1
        result = max(distance[i], result)

print(cnt - 1, result)

'''
[input]
3 2 1
1 2 4
1 3 2

[output]
2 4
'''
