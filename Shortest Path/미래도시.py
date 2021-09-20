'''1->K->X'''
import heapq

INF = int(1e9)
result = 0

def dij(graph, start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, node = heapq.heappop(heap)

        if distance[node] < cost:
            continue

        for temp_cost, temp_node in graph[node]:
            new_cost = cost + temp_cost

            if new_cost < distance[temp_node]:
                distance[temp_node] = new_cost
                heapq.heappush(heap, ((new_cost, temp_node)))
    return distance


# 전체 회사의 개수,경로의 개수
n, m = map(int, input().split())

# 회사 그래프 정보
graph = [[] for _ in range(n + 1)]
# 1에서 K까지의 최단 경로

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

# X,K
X, K = map(int, input().split())

# 1에서 K까지의 최단경로
temp = dij(graph, 1)
result += temp[K]

# K에서 X까지의 최단 경로
temp = dij(graph, K)
result += temp[X]

if result >= INF:
    print(-1)
else:
    print(result)

'''
[input1]
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

[output1]
3

[input2]
4 2
1 3
2 4
3 4

[output2]
-1


'''
