'''cycle 발생 확인 (무향 그래프에서만 가능)'''

def find_parent(parent,x):
    if parent[x]!=x:
        find_parent(parent,parent[x])

    return parent[x]

def union_parent(a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드의 개수, 간선의 개수
v,e=map(int,input().split())
parent=[0]*(v+1)

#자기자신으로 부모테이블 초기화
for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        print("사이클이 발생했습니다.")
        break
    else:
        union_parent(a,b)

'''
[input]
3 3
1 2
1 3
2 3

[output]
사이클이 발생했습니다.
'''
