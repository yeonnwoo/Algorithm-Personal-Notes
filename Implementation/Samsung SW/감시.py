'''
permutations(순열)이 메모리 문제 때문에 해결이 안되는 경우
--> DFS 사용
'''
from copy import deepcopy

dx=[-1,1,0,0]
dy=[0,0,-1,1]
di=[0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,3],[3,1],[2,1],[0,2]],[[2,0,3],[0,3,1],[2,1,3],[0,2,1]],[[0,1,2,3]]]

def DFS(n,graph,CCTV):
    global Min
    if n==len(CCTV):
        cnt = 0
        for ptr in graph:
            cnt += len([i for i in ptr if i == 0])

        if Min > cnt:
            Min = cnt

        return

    #CCTV의 타입,x좌표,y좌표
    type,x,y=CCTV[n]
    for dir in di[type]:
        temp_graph=deepcopy(graph)
        for i in dir:
            xx=x+dx[i]
            yy=y+dy[i]

            while True:
                if xx<0 or yy<0 or xx>=N or yy>=M or temp_graph[xx][yy]==6:
                    break

                if temp_graph[xx][yy]==0:
                    temp_graph[xx][yy]='#'

                xx+=dx[i]
                yy+=dy[i]

        #가지치기가 되는 부분
        DFS(n+1,temp_graph,CCTV)

N,M=map(int,input().split())
Min=N*M
graph=[]
CCTV=[]
dir=[]

for i in range(N):
    L=list(map(int,input().split()))
    for j in range(M):
        if L[j]!=0 and L[j]!=6:
            CCTV.append([L[j],i,j])

    graph.append(L)

#최소 사각지대 찾기
DFS(0,graph,CCTV)

print(Min)

