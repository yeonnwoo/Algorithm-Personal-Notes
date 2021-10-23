def check_out(a,b):
    if a<0 or b<0 or a>=N or b>=N:
        return True

    return False

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

#왼,아래,오,위
dx=[0,1,0,-1]
dy=[-1,0,1,0]

k=1 #반복 증가 횟수
result=0 #밖으로 나온 먼지의 양
x=N//2
y=N//2
dir=0 #방향(왼쪽부터 시작)


for i in range(1,N): #i칸 이동
    for j in range(2):
        for k in range(i):
            x = x + dx[dir]
            y = y + dy[dir]

            if graph[x][y]==0:
                continue

            #왼쪽 방향
            if dir==0:
                #모래의 양
                dust=graph[x][y]
                graph[x][y]=0

                #흩어진 모래의 양
                cnt=0

                #2%
                if check_out(x-2,y):
                    result+=int(dust*(0.02))
                else:
                    graph[x-2][y]+=int(dust*(0.02))
                cnt+=int(dust*0.02)

                #10%
                if check_out(x-1,y-1):
                    result+=int(dust*0.10)
                else:
                    graph[x-1][y-1]+=int(dust*0.10)
                cnt+=int(dust*0.10)

                #7%
                if check_out(x-1,y):
                    result+=int(dust*0.07)
                else:
                    graph[x-1][y]+=int(dust*0.07)
                cnt+=int(dust*0.07)

                #1%
                if check_out(x-1,y+1):
                    result+=int(dust*0.01)
                else:
                    graph[x-1][y+1]+=int(dust*0.01)
                cnt+=int(dust*0.01)

                #5%
                if check_out(x,y-2):
                    result+=int(dust*0.05)
                else:
                    graph[x][y-2]+=int(dust*0.05)
                cnt+=int(dust*0.05)

                #10%
                if check_out(x+1,y-1):
                    result+=int(dust*0.10)
                else:
                    graph[x+1][y-1]+=int(dust*0.10)
                cnt+=int(dust*0.10)

                #7%
                if check_out(x+1,y):
                    result += int(dust * 0.07)
                else:
                    graph[x + 1][y] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                #1%
                if check_out(x+1,y+1):
                    result += int(dust * 0.01)
                else:
                    graph[x + 1][y+1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                #2%
                if check_out(x+2,y):
                    result += int(dust * 0.02)
                else:
                    graph[x + 2][y] += int(dust * 0.02)
                cnt += int(dust * 0.02)

                #나머지
                if check_out(x,y-1):
                    result+=int(dust-cnt)
                else:
                    graph[x][y-1]+=int(dust-cnt)

            #아래 방향
            elif dir==1:
                # 모래의 양
                dust = graph[x][y]
                graph[x][y] = 0

                # 흩어진 모래의 양
                cnt = 0

                # 2%
                if check_out(x, y-2):
                    result += int(dust * (0.02))
                else:
                    graph[x][y-2] += int(dust * (0.02))

                cnt += int(dust * 0.02)

                # 10%
                if check_out(x +1, y - 1):
                    result += int(dust * 0.10)
                else:
                    graph[x + 1][y - 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x, y-1):
                    result += int(dust * 0.07)
                else:
                    graph[x][y-1] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x - 1, y - 1):
                    result += int(dust * 0.01)
                else:
                    graph[x - 1][y - 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 5%
                if check_out(x+2, y):
                    result += int(dust * 0.05)
                else:
                    graph[x+2][y] += int(dust * 0.05)
                cnt += int(dust * 0.05)

                # 10%
                if check_out(x + 1, y + 1):
                    result += int(dust * 0.10)
                else:
                    graph[x + 1][y + 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x, y+1):
                    result += int(dust * 0.07)
                else:
                    graph[x][y+1] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x - 1, y + 1):
                    result += int(dust * 0.01)
                else:
                    graph[x - 1][y + 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 2%
                if check_out(x, y+2):
                    result += int(dust * 0.02)
                else:
                    graph[x][y+2] += int(dust * 0.02)
                cnt += int(dust * 0.02)

                # 나머지
                if check_out(x+1, y):
                    result += int(dust - cnt)
                else:
                    graph[x+1][y] += int(dust - cnt)

            #오른쪽
            elif dir==2:
                # 모래의 양
                dust = graph[x][y]
                graph[x][y] = 0

                # 흩어진 모래의 양
                cnt = 0

                # 2%
                if check_out(x +2, y):
                    result += int(dust * (0.02))
                else:
                    graph[x + 2][y] += int(dust * (0.02))

                cnt += int(dust * 0.02)

                # 10%
                if check_out(x + 1, y + 1):
                    result += int(dust * 0.10)
                else:
                    graph[x + 1][y + 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x + 1, y):
                    result += int(dust * 0.07)
                else:
                    graph[x + 1][y] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x + 1, y - 1):
                    result += int(dust * 0.01)
                else:
                    graph[x + 1][y - 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 5%
                if check_out(x, y + 2):
                    result += int(dust * 0.05)
                else:
                    graph[x][y + 2] += int(dust * 0.05)
                cnt += int(dust * 0.05)

                # 10%
                if check_out(x - 1, y + 1):
                    result += int(dust * 0.10)
                else:
                    graph[x - 1][y + 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x - 1, y):
                    result += int(dust * 0.07)
                else:
                    graph[x -1][y] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x - 1, y - 1):
                    result += int(dust * 0.01)
                else:
                    graph[x - 1][y - 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 2%
                if check_out(x - 2, y):
                    result += int(dust * 0.02)
                else:
                    graph[x - 2][y] += int(dust * 0.02)
                cnt += int(dust * 0.02)

                # 나머지
                if check_out(x, y + 1):
                    result += int(dust - cnt)
                else:
                    graph[x][y + 1] += int(dust - cnt)

            #위쪽
            else:
                # 모래의 양
                dust = graph[x][y]
                graph[x][y] = 0

                # 흩어진 모래의 양
                cnt = 0

                # 2%
                if check_out(x, y-2):
                    result += int(dust * (0.02))
                else:
                    graph[x][y-2] += int(dust * (0.02))

                cnt += int(dust * 0.02)

                # 10%
                if check_out(x - 1, y - 1):
                    result += int(dust * 0.10)
                else:
                    graph[x - 1][y - 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x, y-1):
                    result += int(dust * 0.07)
                else:
                    graph[x][y-1] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x +1, y - 1):
                    result += int(dust * 0.01)
                else:
                    graph[x + 1][y - 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 5%
                if check_out(x-2, y):
                    result += int(dust * 0.05)
                else:
                    graph[x-2][y] += int(dust * 0.05)
                cnt += int(dust * 0.05)

                # 10%
                if check_out(x - 1, y + 1):
                    result += int(dust * 0.10)
                else:
                    graph[x - 1][y + 1] += int(dust * 0.10)
                cnt += int(dust * 0.10)

                # 7%
                if check_out(x, y+1):
                    result += int(dust * 0.07)
                else:
                    graph[x][y+1] += int(dust * 0.07)
                cnt += int(dust * 0.07)

                # 1%
                if check_out(x + 1, y + 1):
                    result += int(dust * 0.01)
                else:
                    graph[x + 1][y + 1] += int(dust * 0.01)
                cnt += int(dust * 0.01)

                # 2%
                if check_out(x, y+2):
                    result += int(dust * 0.02)
                else:
                    graph[x][y+2] += int(dust * 0.02)
                cnt += int(dust * 0.02)

                # 나머지
                if check_out(x-1, y):
                    result += int(dust - cnt)
                else:
                    graph[x-1][y] += int(dust - cnt)

        dir+=1

        if dir>3:
            dir=dir%4


for i in range(N-1):
    x += dx[0]
    y += dy[0]

    #왼쪽 방향
    #모래의 양
    dust=graph[x][y]
    graph[x][y] = 0

    #흩어진 모래의 양
    cnt=0

    # 2%
    if check_out(x - 2, y):
        result += int(dust * (0.02))
    else:
        graph[x - 2][y] += int(dust * (0.02))
    cnt += int(dust * 0.02)

    # 10%
    if check_out(x - 1, y - 1):
        result += int(dust * 0.10)
    else:
        graph[x - 1][y - 1] += int(dust * 0.10)
    cnt += int(dust * 0.10)

    # 7%
    if check_out(x - 1, y):
        result += int(dust * 0.07)
    else:
        graph[x - 1][y] += int(dust * 0.07)
    cnt += int(dust * 0.07)

    # 1%
    if check_out(x - 1, y + 1):
        result += int(dust * 0.01)
    else:
        graph[x - 1][y + 1] += int(dust * 0.01)
    cnt += int(dust * 0.01)

    # 5%
    if check_out(x, y - 2):
        result += int(dust * 0.05)
    else:
        graph[x][y - 2] += int(dust * 0.05)
    cnt += int(dust * 0.05)

    # 10%
    if check_out(x + 1, y - 1):
        result += int(dust * 0.10)
    else:
        graph[x + 1][y - 1] += int(dust * 0.10)
    cnt += int(dust * 0.10)

    # 7%
    if check_out(x + 1, y):
        result += int(dust * 0.07)
    else:
        graph[x + 1][y] += int(dust * 0.07)
    cnt += int(dust * 0.07)

    # 1%
    if check_out(x + 1, y + 1):
        result += int(dust * 0.01)
    else:
        graph[x + 1][y + 1] += int(dust * 0.01)
    cnt += int(dust * 0.01)

    # 2%
    if check_out(x + 2, y):
        result += int(dust * 0.02)
    else:
        graph[x + 2][y] += int(dust * 0.02)
    cnt += int(dust * 0.02)

    # 나머지
    if check_out(x, y - 1):
        result += int(dust - cnt)
    else:
        graph[x][y - 1] += int(dust - cnt)



print(result)