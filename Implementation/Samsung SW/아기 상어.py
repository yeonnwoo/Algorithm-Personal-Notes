from collections import deque

def shark(px,py,graph,size):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    Time=0
    eat_cnt = 0

    while True:
        que = deque()
        que.append((px, py, 0))
        visited = set()
        visited.add((px, py))
        List = []
        check=1e9

        while que:
            x,y,cnt=que.popleft()

            if check<cnt:
                break

            for k in range(4):
                xx=dx[k]
                yy=dy[k]

                if x+xx<0 or y+yy<0 or x+xx>=N or y+yy>=N:
                    continue

                if (x+xx,y+yy) in visited or graph[x+xx][y+yy]>size:
                    continue

                if graph[x+xx][y+yy]<size and graph[x+xx][y+yy]!=0:
                    List.append((cnt+1, x + xx, y + yy))
                    check=cnt

                que.append((x + xx, y + yy, cnt + 1))
                visited.add((x+xx,y+yy))

        if len(List)!=0:
            List=sorted(List,key=lambda x:(x[0],x[1],x[2]))
            cnt,x,y=List[0][0],List[0][1],List[0][2]

            Time+=cnt
            eat_cnt+=1
            graph[x][y]=0

            px,py=x,y
            if eat_cnt==size:
                size+=1
                eat_cnt=0

        else:
            break

    return Time


#공간의 크기
N=int(input())
graph=[]
x=0
y=0
size=2

for i in range(N):
    List=list(map(int,input().split()))
    graph.append(List)

    if 9 in List:
        x=i
        y=List.index(9)
        graph[x][y]=0

if [[0]*N for _ in range(N)]==graph:
    print(0)
else:
    print(shark(x,y,graph,size))