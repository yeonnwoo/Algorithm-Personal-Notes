'''Topology sort'''

n=int(input())
indegree=[0]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(n):
    List=list(map(int,input().split()))
    Time=List[0]
    


'''
[input]
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

[output]
10
20
14
18
17
'''