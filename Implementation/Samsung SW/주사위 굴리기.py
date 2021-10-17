def dir_change(i):
    if i==1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif i==2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif i==3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


#동,서,북,남(1,2,3,4)
dx=[0,0,-1,1]
dy=[1,-1,0,0]

dice={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

N,M,x,y,K=map(int,input().split())
graph=[]
List=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
List=list(map(int,input().split()))

for dir in List:
    x+=dx[dir-1]
    y+=dy[dir-1]

    if x < 0 or y < 0 or x >= N or y >= M:
        x -= dx[dir-1]
        y -= dy[dir-1]
        continue

    dir_change(dir)

    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0

    print(dice[1])