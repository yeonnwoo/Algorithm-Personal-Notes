def find_like(target,Like,graph):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    List=[]
    Max=0

    for x in range(N):
        for y in range(N):
            if graph[x][y]==0:
                cnt=0 # 주변에 좋아하는 사람의 수
                cnt_0=0 # 주변에 비어있는 자리 개수
                for k in range(4):
                    xx=dx[k]
                    yy=dy[k]

                    if x+xx<0 or y+yy<0 or x+xx>=N or y+yy>=N:
                        continue

                    if graph[x+xx][y+yy] in Like:
                        cnt+=1

                    if graph[x+xx][y+yy]==0:
                        cnt_0+=1

                if Max<=cnt:
                    Max=cnt
                    List.append((x,y,cnt_0,cnt))

    List=sorted(List,key=lambda x:(-x[3],-x[2],x[0],x[1]))
    a=List[0][0]
    b=List[0][1]

    graph[a][b]=target

N=int(input())
graph=[[0]*N for _ in range(N)]
#자신이 좋아하는 사람
dic={}

for _ in range(N**2):
    List=list(map(int,input().split()))
    dic[List[0]]=List[1:]


#자리 하나씩 찾아나서기
'''
1. 그래프 탐색하여 자신이 좋아하는 사람이 가장 많은 곳으로 앉기
2. (1)의 '횟수가 모두 0'이거나 '여러 곳' 이라면 상하좌우가 0인 곳이 가장 많은 곳에 앉기
3. (2)의 경우가 여러 곳이라면 이중에 행의 번호가 가장 작은 곳으로
4. (3)의 경우가 여러 곳이라면 이중에 열의 번호가 가장 작은 곳으로
'''

for key,val_list in dic.items():
    find_like(key,val_list,graph)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0

for i in range(N):
    for j in range(N):
        target=graph[i][j]
        cnt=0
        for k in range(4):
            xx=dx[k]
            yy=dy[k]

            if i+xx<0 or j+yy<0 or i+xx>=N or j+yy>=N:
                continue

            if graph[i+xx][j+yy] in dic[target]:
                cnt+=1

        if cnt==1:
            result+=1
        elif cnt==2:
            result+=10
        elif cnt==3:
            result+=100
        elif cnt==4:
            result+=1000

print(result)