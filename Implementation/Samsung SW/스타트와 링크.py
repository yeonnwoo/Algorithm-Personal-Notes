from itertools import combinations

N=int(input())
graph=[]
team=[i for i in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

combination=list(combinations(team,N//2))
visited=set()
Min=100*20

for c in range(len(combination)):
    cnt1=0
    cnt2=0
    team_A=combination[c]
    team_B = tuple(set(team)-(set(team_A)))

    if team_A not in visited:
        visited.add(team_A)
        visited.add(team_B)

        for i in range(len(team_A)-1):
            for j in range(i+1,len(team_A)):
                cnt1+=graph[team_A[i]][team_A[j]]+graph[team_A[j]][team_A[i]]
                cnt2+=graph[team_B[i]][team_B[j]]+graph[team_B[j]][team_B[i]]

        if abs(cnt1-cnt2)<Min:
            Min=abs(cnt1-cnt2)

print(Min)

