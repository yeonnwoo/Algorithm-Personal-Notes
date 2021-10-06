def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

N,M=map(int,input().split())
graph=[]
parent=[0]*(N+1)

for i in range(1,N+1):
    parent[i]=i

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j]==1:
            union(parent,i,j)

path=list(map(int,input().split()))
check=0

for i in range(M-1):
    now=path[i]
    after=path[i+1]

    if find_parent(parent,now) != find_parent(parent,after):
        print("NO")
        check=-1
        break

if check==0:
    print("YES")

'''
[input]
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

[output]
YES
'''





