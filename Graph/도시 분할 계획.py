'''Kruskal'''

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m= map(int,input().split())
graph=[]
result=[]

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i

for _ in range(m):
    a,b,c=map(int,input().split())
    graph.append((c,a,b))

graph.sort()

for cost,a,b in graph:
    if find_parent(parent,a)!=find_parent(parent,b):
        result.append(cost)
        union_parent(parent,a,b)

result.pop()
print(sum(result))

'''
[input]
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

[output]
8
'''