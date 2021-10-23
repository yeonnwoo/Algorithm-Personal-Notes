from collections import Counter
import copy


r,c,K=map(int,input().split())
graph=[[0]*100 for _ in range(100)]
check=0

for i in range(3):
    List=list(map(int,input().split()))
    for j in range(3):
        graph[i][j]=List[j]


#100초가 지나도 graph[r][c]=k이 아니면 -1 출력
n=3 #행의 개수
m=3 #열의 개수
for Time in range(101):

    if graph[r-1][c-1]==K:
        print(Time)
        check=1
        break

    #행의 개수>=열의 개수일 때
    if n>=m:
        new_graph=[]
        for i in range(n):
            List=graph[i]
            if sum(List)!=0:
                counter=dict(Counter(List))
                counter.pop(0)
                counter=sorted(counter.items(),key=lambda x:(x[1],x[0]))

                k=0
                for j in range(len(counter)):
                    graph[i][k]=counter[j][0]
                    k+=1
                    graph[i][k]=counter[j][1]
                    k+=1

                #graph[i]=graph[i][:len(counter)*2]+[0]*(100-len(counter)*2)

                for p in range(len(counter)*2,100):
                    graph[i][p]=0


                #열의 값 업데이트
                if m<len(counter)*2:
                    m=len(counter)*2

    else:
        temp=copy.deepcopy(graph)
        temp=list(map(list,zip(*temp)))

        for i in range(m):
            List=temp[i]
            if sum(List)!=0:
                counter=dict(Counter(List))
                counter.pop(0)
                counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))

                k=0
                for j in range(len(counter)):
                    graph[k][i]=counter[j][0]
                    k+=1
                    graph[k][i]=counter[j][1]
                    k+=1

                #graph[i] = graph[:len(counter) * 2][i] + [0] * (100 - len(counter) * 2)

                for p in range(len(counter) * 2, 100):
                    graph[p][i] = 0

                # 열의 값 업데이트
                if n < len(counter) * 2:
                    n = len(counter) * 2


if check==0:
    print(-1)