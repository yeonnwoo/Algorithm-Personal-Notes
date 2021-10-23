import heapq
from collections import deque
import copy

def fish_move(shark_x,shark_y):

    global fish
    global graph

    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,-1,-1,-1,0,1,1,1]
    temp_fish=[]

    while fish:
        fish.sort()
        num,x,y=heapq.heappop(fish)
        dir=graph[x][y][1]

        for _ in range(8):
            xx=dx[dir]
            yy=dy[dir]

            if x+xx<0 or y+yy<0 or x+xx>=4 or y+yy>=4 or (x+xx==shark_x and y+yy==shark_y):
                dir+=1

                if dir>7:
                    dir=(dir)%8

            else:
                a=graph[x+xx][y+yy] #바뀜 당하는 애
                b=graph[x][y] #바뀌어 지는 애

                #바뀜 당하는 애 좌표 바꿔주기
                if (graph[x+xx][y+yy][0],x+xx,y+yy) in fish:
                    fish.remove((graph[x+xx][y+yy][0],x+xx,y+yy))
                    heapq.heappush(fish,(graph[x+xx][y+yy][0],x,y))

                graph[x][y]=a
                graph[x+xx][y+yy]=(b[0],dir)

                heapq.heappush(temp_fish,(num,x+xx,y+yy))
                break
    fish=temp_fish

    return graph


def shark(graph,shark_x,shark_y,shark_dir,first_result,temp_fish):

    global fish

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    real_graph=copy.deepcopy(graph) #(0,0)만 먹은 원본

    Max=0

    for pp in range(3):
        dir=shark_dir
        x = shark_x
        y = shark_y
        result=first_result

        stack=deque()
        xx=dx[dir]*(pp+1)
        yy=dy[dir]*(pp+1)
        graph=copy.deepcopy(real_graph)
        s_fish=copy.deepcopy(temp_fish)

        print("x,y:", x+xx, y+yy)

        #4번 안에 먹을게 없음
        if x+xx<0 or y+yy<0 or x+xx>=4 or y+yy>=4:
            break

        num = graph[x + xx][y + yy][0] #물고기 숫자
        new_dir=graph[x+xx][y+yy][1] # 잡아먹은 물고기 방향

        print("num,new_dir",num,new_dir)

        #먹음
        stack.append((x+xx,y+yy,new_dir,result+num))
        graph[x+xx][y+yy]=(0,0)

        #물고기 이동
        graph=fish_move(x+xx, y+yy)

        #두번째까지 이동한 후의 그래프
        temp_graph=copy.deepcopy(graph)
        t_fish=copy.deepcopy(fish)

        #DFS
        while stack:
            x, y, dir, result = stack.pop()
            print("pop후:",result)

            xx=dx[dir]
            yy=dy[dir]

            if x+xx<0 or y+yy<0 or x+xx>=4 or y+yy>=4:
                if Max<result:
                    Max=result

                print("result:",result)

                graph=copy.deepcopy(temp_graph)
                continue

            num=graph[x+xx][y+yy][0]
            new_dir=graph[x+xx][y+yy][1]

            #먹음
            print("x,y,result:",x,y, result)
            stack.append((x+xx,y+yy,new_dir,result+num))

            graph[x+xx][y+yy]=(0,0)

            print("물고기 이동전:",graph)
            #상어의 위치
            graph=fish_move(x+xx, y+yy)
            print("물고기 이동 후:",graph)

    return Max

    # while stack:
    #     x,y,dir,result=stack.pop()
    #
    #     #해당 방향에 있는 물고기 모두 저장
    #     for _ in range(4):
    #         xx=dx[dir]
    #         yy=dy[dir]
    #
    #         if x+xx<0 or y+yy<0 or x+xx>=4 or y+yy>=4:
    #             print("result:",result)
    #             print(graph)
    #             if Max<result:
    #                 Max=result
    #
    #             graph=copy.deepcopy(real_graph)
    #             continue
    #
    #         num=graph[x+xx][y+yy][0]
    #         new_dir=graph[x+xx][y+yy][1]
    #
    #         #먹음
    #         stack.append((x+xx,y+yy,new_dir,result+num))
    #         graph[x+xx][y+yy]=(0,0)
    #
    #         fish=fish_move(graph, fish, x+xx, y+yy)
    #
    #
    # return Max

graph=[]
fish=[]

for i in range(4):
    List=list(map(int,input().split()))
    temp=[]
    for j in range(4):
        temp.append((List[2*j],List[2*j+1]-1)) #번호,방향
        fish.append((List[2*j],i,j)) #물고기 번호,x좌표,y좌표

    graph.append(temp)



result=0
result+=graph[0][0][0] #물고기 번호
shark_dir=graph[0][0][1] #상어의 첫번째 방향
shark_x=0
shark_y=0
#(0,0) 위치의 물고기 삭제
fish.remove((graph[0][0][0],0,0))

graph[0][0]=(0,0) # 상어가 먹음

graph=fish_move(shark_x,shark_y)

temp_fish=copy.deepcopy(fish)

print("====",temp_fish)

print(shark(graph,shark_x,shark_y,shark_dir,result,temp_fish))