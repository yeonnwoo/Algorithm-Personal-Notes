from collections import deque
import sys

N,M,K,X=map(int,sys.stdin.readline().rstrip().split())
graph={i:[] for i in range(N+1)}
distance=[-1]*(N+1)
distance[X]=0

for _ in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

que=deque()
que.append(X)

while que:
    q=que.popleft()

    for data in graph[q]:
        if distance[data]==-1:
            distance[data]=distance[q]+1
            que.append(data)

result=[i for i in range(len(distance)) if distance[i]==K]

if len(result)==0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

'''
[input]
4 4 2 1
1 2
1 3
3 4
2 4

[output]
4
'''