'''Union-Find'''

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

N,M=map(int,input().split())
parent=[0]*(N+1)

#parent 초기화
for i in range(N+1):
    parent[i]=i

for _ in range(M):
    check,a,b=map(int,input().split())

    if check==0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a)!=find_parent(parent,b):
            print("NO")
        else:
            print("YES")

'''
[input]
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

[output]
NO
NO
YES
'''