from itertools import product
import copy

def move_up(graph):
    for y in range(N):
        ptr = 0 #0의 위치
        target=0
        for x in range(N):
            if graph[x][y]==0:
                continue
            else:
                if target==0:
                    target=graph[x][y]
                else:
                    if graph[x][y]==target:
                        graph[ptr][y]=target*2
                        ptr+=1
                        target=0
                    else:
                        graph[ptr][y]=target
                        ptr += 1
                        target=graph[x][y]

            graph[x][y]=0

        if target!=0:
            graph[ptr][y]=target

    return graph

def move_down(graph):
    for y in range(N):
        ptr=N-1
        target=0
        for x in range(N-1,-1,-1):
            if graph[x][y]==0:
                continue
            else:
                if target==0:
                    target=graph[x][y]
                else:
                    if target==graph[x][y]:
                        graph[ptr][y]=target*2
                        ptr-=1
                        target=0
                    else:
                        graph[ptr][y]=target
                        ptr-=1
                        target=graph[x][y]
            graph[x][y]=0

        if target!=0:
            graph[ptr][y]=target

    return graph

def move_left(graph):
    for x in range(N):
        target=0
        ptr=0
        for y in range(N):
            if graph[x][y]==0:
                continue
            else:
                if target==0:
                    target=graph[x][y]
                else:
                    if target==graph[x][y]:
                        graph[x][ptr]=target*2
                        ptr+=1
                        target=0
                    else:
                        graph[x][ptr]=target
                        target=graph[x][y]
                        ptr+=1

            graph[x][y]=0

        if target!=0:
            graph[x][ptr]=target

    return graph

def move_right(graph):
    for x in range(N):
        ptr=N-1
        target=0
        for y in range(N-1,-1,-1):
            if graph[x][y]==0:
                continue
            else:
                if target==0:
                    target=graph[x][y]
                else:
                    if target==graph[x][y]:
                        graph[x][ptr]=target*2
                        ptr-=1
                        target=0
                    else:
                        graph[x][ptr]=target
                        target=graph[x][y]
                        ptr-=1

            graph[x][y]=0

        if target!=0:
            graph[x][ptr]=target

    return graph

N=int(input())
L=[1,2,3,4] #상,하,좌,우
graph=[]
Max=0
for _ in range(N):
    graph.append(list(map(int,input().split())))

products=product(L,repeat=5)

for pro in products:
    temp_graph = copy.deepcopy(graph)
    for dir in pro:
        if dir==1:
            temp_graph=move_up(temp_graph)
        elif dir==2:
            temp_graph=move_down(temp_graph)
        elif dir==3:
            temp_graph=move_left(temp_graph)
        else:
            temp_graph=move_right(temp_graph)

        Max=max(Max,max([max(i) for i in temp_graph]))

print(Max)