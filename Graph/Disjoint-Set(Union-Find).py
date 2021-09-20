'''Disjoint-Set (Union-Find)'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수,간선의 개수
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent,a, b)

for i in range(1,v+1):
    find_parent(parent,i)

print(parent)

'''
[input]
6 4
1 4
2 3
2 4
5 6

[output]
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 1 1 5 5
'''
