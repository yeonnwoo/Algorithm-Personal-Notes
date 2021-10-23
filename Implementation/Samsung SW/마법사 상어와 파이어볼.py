import copy
from collections import deque

N, M, K = map(int, input().split())  # 크기,파이어볼 M개 발사,이동 K번 명령
graph = [[deque() for _ in range(N)] for _ in range(N)]

temp = []  # 파이어볼 들어있는 곳

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    List = list(map(int, input().split()))
    temp.append((List[0] - 1, List[1] - 1))
    graph[List[0] - 1][List[1] - 1].append(List[2:])  # 질량,속력,방향

# K번 이동시작
for _ in range(K):
    temp_graph = copy.deepcopy(graph)
    # 파이어볼 이동
    for x in range(N):
        for y in range(N):

            if len(graph[x][y]) == 0:
                continue

            while graph[x][y]:
                m, speed, dir = graph[x][y].popleft()
                temp_graph[x][y].popleft()

                # 질량이 0인 파이어볼 소멸
                if m == 0:
                    temp_graph[x][y].remove([m, speed, dir])

                # 이동
                xx = dx[dir] * speed
                yy = dy[dir] * speed

                xxx = x + xx
                yyy = y + yy

                # 범위를 벗어남
                if xxx < 0:
                    if 1 <= abs(xxx) <= 4:
                        xxx = N + (xxx)
                    else:
                        xxx = abs(xxx) % N
                        xxx = N - xxx

                if xxx >= N:
                    xxx = xxx % N

                if yyy < 0:
                    if 1 <= abs(yyy) <= 4:
                        yyy = N + (yyy)
                    else:
                        yyy = abs(yyy) % N
                        yyy = N - yyy

                if yyy >= N:
                    yyy = yyy % N

                temp_graph[xxx][yyy].append(deque([m, speed, dir]))

    graph = temp_graph

    # 두개 이상의 파이어볼이 있는 경우
    for i in range(N):
        for j in range(N):
            temp_List = graph[i][j]

            if len(temp_List) < 2:
                continue

            m_sum = 0
            dir_1 = 0  # 홀수합
            dir_2 = 0  # 짝수합
            speed_sum = 0
            n = len(temp_List)  # 파이어볼의 개수

            for temp_m, temp_s, temp_d in temp_List:
                m_sum += temp_m
                speed_sum += temp_s
                if temp_d % 2 == 0:
                    dir_2 += 1
                else:
                    dir_1 += 1

            final_m = m_sum // 5
            if final_m==0:
                graph[i][j]=deque()
            final_s = speed_sum // n
            final_dir = []

            # 모두 짝수이거나 홀수
            if dir_1==n or dir_2==n:
                final_dir = [0, 2, 4, 6]
            else:
                final_dir = [1, 3, 5, 7]

            # 4개로 나누기
            graph[i][j] = deque([[final_m, final_s, final_dir[0]], [final_m, final_s, final_dir[1]],
                                 [final_m, final_s, final_dir[2]], [final_m, final_s, final_dir[3]]])

result = 0
for i in range(N):
    for j in range(N):
        for List in graph[i][j]:
            result += List[0]

print(result)
