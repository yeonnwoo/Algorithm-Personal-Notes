from collections import deque

'''Depth First Search (DFS) '''
def DFS(graph, s):
    stack = deque()
    visited = set()
    stack.append(s)

    while stack:
        q = stack.pop()
        if q not in visited:
            print(q, end=" ")
        visited.add(q)
        graph[q].sort(reverse=True)
        for node in graph[q]:
            if node not in visited:
                stack.append(node)
    print("")

''' Breadth First Search (BFS) '''
def BFS(graph, s):
    que = deque()
    visited = set()
    que.append(s)
    visited.add(s)

    while que:
        q = que.popleft()
        print(q, end=" ")

        graph[q].sort()
        for node in graph[q]:
            if node not in visited:
                que.append(node)
                visited.add(node)

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(graph, V)
BFS(graph, V)

'''
[Input Example 1]
4 5 1
1 2
1 3
1 4
2 4
3 4
[Output Example 1]
1 2 4 3 
1 2 3 4
'''
