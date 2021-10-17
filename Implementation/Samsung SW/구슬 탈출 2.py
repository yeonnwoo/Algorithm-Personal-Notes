from collections import deque

N,M=map(int,input().split())
graph=[]
red_x=0
red_y=0
blue_x=0
blue_y=0
cnt=0
check=-1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    List=list(input())
    if 'R' in List:
        red_x=i
        red_y=List.index('R')
    if 'B' in List:
        blue_x=i
        blue_y=List.index('B')
    graph.append(List)

stack=deque()
visited=set()
distance=[]

#빨간 구슬이 구멍에 들어갈 수 있는 경로
stack.append((red_x,red_y))

print(graph)
print("빨간 공 위치: ", (red_x,red_y))
print("파란 공 위치: ", (blue_x,blue_y))

while stack:
    x,y=stack.pop()
    visited.add((x,y))

    for i in range(4):
        xx=dx[i]
        yy=dy[i]

        if x+xx<0 or yy+y<0 or x+xx>=N or y+yy>=M:
            continue

        #빨간 구슬이 벽을 만날 때까지 이동
        if graph[x+xx][y+yy]=='.':
            cnt+=1
            red_x=x+xx
            red_y=y+yy

            # 끝까지 이동
            while True:
                if red_x<0 or red_y<0 or red_x>=N or red_y>=M\
                        or graph[red_x][red_y]=='#' or graph[red_x][red_y]=='B':
                    red_x-=xx
                    red_y-=yy
                    break

                elif graph[red_x][red_y]=='O':
                    #빨간공 들어감
                    check=0

                red_x+=xx
                red_y+=yy


            # 파란 구슬 이동
            if graph[blue_x+xx][blue_y+yy]=='.':
                blue_x+=xx
                blue_y+=yy

                if blue_x<0 or blue_y<0 or blue_x>=N or blue_y>=M:
                    continue

                while True:
                    if graph[blue_x][blue_y]=='R' or graph[blue_x][blue_y]=='#':
                        break
                    elif graph[blue_x][blue_y]=='O':
                        cnt=0
                        # 빨간공과 파란공이 동시에 들어감
                        if check==0:
                            check=-1
                            break


            #빨간공 경로 추가
            print("빨간 공 위치: ", (red_x,red_y))
            print("파란 공 위치: ", (blue_x,blue_y))
            stack.append((red_x,red_y))

if check==0:
    print(cnt)
elif check==-1 or cnt>10:
    print(-1)








