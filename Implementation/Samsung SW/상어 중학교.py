from collections import deque

def find_group(graph):
    global result

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    List=[]
    cnt=0

    for i in range(N):
        for j in range(N):
            if 1<=graph[i][j]<=M:
                target=graph[i][j]
                que=deque()
                visited=set()
                cnt=1
                cnt_mu=0 #무지개 개수

                que.append((i,j))
                visited.add((i,j))

                while que:
                    x,y=que.popleft()

                    for k in range(4):
                        xx=dx[k]
                        yy=dy[k]

                        if x+xx<0 or y+yy<0 or x+xx>=N or y+yy>=N:
                            continue

                        if (x+xx,y+yy) not in visited:
                            if graph[x+xx][y+yy]==target or graph[x+xx][y+yy]==0:
                                que.append((x+xx,y+yy))
                                visited.add((x+xx,y+yy))
                                cnt+=1
                                if graph[x+xx][y+yy]==0:
                                    cnt_mu+=1

                List.append([cnt,cnt_mu,i,j,visited])

    List=sorted(List,key=lambda x:(-x[0],-x[1],-x[2],-x[3]))

    if len(List)!=0:
        if List[0][0]>=2:
            temp=List[0][4]
            result+=List[0][0]**2
            for i, j in temp:
                graph[i][j] = -2  # 빈칸
            return graph

    # 더이상 그룹이 존재하지 않음
    return False

def get_gravity(graph):
    for y in range(N):
        for x in range(N-2,-1,-1):
            if graph[x][y]>=0:
                ptr=x
                while True:
                    ptr += 1
                    if ptr>=N:
                        ptr-=1
                        break
                    if graph[ptr][y]!=-2:
                        ptr-=1
                        break


                if ptr!=x:
                    graph[ptr][y]=graph[x][y]
                    graph[x][y]=-2

    return graph

def get_cycle(graph):
    new_graph=[[0]*N for _ in range(N)]
    i=0
    for y in range(N-1,-1,-1):
        j=0
        for x in range(N):
            new_graph[i][j]=graph[x][y]
            j+=1
        i+=1

    return new_graph

#격자의 크기 N, 색상의 개수 M
N,M=map(int,input().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))

result=0

while True:
    #블록 그룹 찾기
    graph=find_group(graph)

    if graph==False:
        break

    #중력 작용
    graph=get_gravity(graph)

    #반시계로 90도 회전
    graph=get_cycle(graph)

    #중력 작용
    graph=get_gravity(graph)

print(result)