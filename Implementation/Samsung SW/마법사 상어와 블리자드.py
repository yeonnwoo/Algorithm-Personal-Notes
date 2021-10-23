import copy

def move(graph):
    start=1
    end=2
    x_start=0
    y_start=0
    x_end=0
    y_end=0

    while start<N*N and end<N*N:
        #0의 자리
        while start<N*N:
            x_start,y_start=dic[start]

            if graph[x_start][y_start]==0:
                break
            start+=1
        else:
            return

        end=start+1
        #0이 아닌 자리
        while end<N*N:
            x_end,y_end=dic[end]

            if graph[x_end][y_end]!=0:
                break
            end+=1

        #더이상 옮길 것이 없음
        else:
            return

        graph[x_start][y_start]=graph[x_end][y_end]
        graph[x_end][y_end] = 0



N,M=map(int,input().split()) #N*N 이고 마법은 M번 실행
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

#방향,거리
magic=[]
for _ in range(M):
    magic.append(list(map(int,input().split())))

dic={}
dx=[0,1,0,-1]
dy=[-1,0,1,0]

kk=1
idx=1
x=N//2
y=N//2
i=0

#인덱스 정보 저장
for _ in range(N-1):
    for j in range(2):
        #1번반복,2번반복..
        for k in range(kk):
            xx=dx[i]
            yy=dy[i]

            x=x+xx
            y=y+yy
            dic[idx]=(x,y)
            idx+=1

        i+=1
        if i>3:
            i=i%4
    kk+=1

for i in range(N-2,-1,-1):
    dic[idx]=(0,i)
    idx+=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#상어있는 자리
x=N//2
y=N//2

ans_1=0 #폭발한 1번 구슬의 개수
ans_2=0
ans_3=0



#마법 실행
for m in range(M):
    dir=magic[m][0]-1
    distance=magic[m][1]

    xx = dx[dir]
    yy = dy[dir]

    #파괴
    temp_x=x
    temp_y=y
    for _ in range(distance):
        temp_x+=xx
        temp_y+=yy

        graph[temp_x][temp_y]=0

    #이동
    move(graph)

    #폭발
    check=1
    while check!=0:
        i=1
        check = 0
        while i<N*N-1:
            j=i+1
            cnt=1
            start_x,start_y=dic[i]

            while j<N*N:
                end_x, end_y = dic[j]
                if graph[start_x][start_y] != graph[end_x][end_y]:
                    break
                cnt+=1
                j+=1

            if cnt>=4 and graph[start_x][start_y]!=0:
                check=1
                if graph[start_x][start_y]==1:
                    ans_1+=cnt
                elif graph[start_x][start_y]==2:
                    ans_2+=cnt
                elif graph[start_x][start_y]==3:
                    ans_3+=cnt

                for a in range(i,j):
                    temp_x,temp_y=dic[a]

                    graph[temp_x][temp_y]=0

            i=j

        #이동
        move(graph)

    #그룹
    temp_graph=[[0]*N for _ in range(N)]

    ptr=1
    i=1
    while i < N * N:
        j = i + 1
        cnt = 1
        start_x, start_y = dic[i]

        while j < N * N:
            end_x, end_y = dic[j]
            if graph[start_x][start_y] != graph[end_x][end_y]:
                break
            cnt += 1
            j += 1

        if graph[start_x][start_y] != 0:
            if ptr<N*N:
                ptr_x,ptr_y=dic[ptr]
                temp_graph[ptr_x][ptr_y]=cnt

                ptr+=1

                ptr_x, ptr_y = dic[ptr]
                temp_graph[ptr_x][ptr_y] =graph[start_x][start_y]
                ptr+=1

        i = j

    graph=copy.deepcopy(temp_graph)

print(1*ans_1+2*ans_2+3*ans_3)