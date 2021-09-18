'''
[시간 제한]
1초
M<=50
O(N^3)으로 해결 가능

[시간 복잡도]
O(N)
'''

cnt = 1
check = 0
xx = 0
yy = 0
graph = []
visited = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
y, x, d = map(int, input().split())

# 0=육지,1=바다
for _ in range(N):
    graph.append(list(map(int, input().split())))

graph[x][y] = 1

while True:
    # 왼쪽으로 돌기
    if d == 0:  # 북쪽->서쪽
        xx = x + dx[2]
        yy = y + dy[2]
        d = 3

    elif d == 1:  # 동쪽-> 북쪽
        xx = x + dx[0]
        yy = y + dy[0]
        d = 0

    elif d == 2:  # 남쪽 -> 동쪽
        xx = x + dx[3]
        yy = y + dy[3]
        d = 1

    else:
        xx = x + dx[1]
        yy = y + dy[1]
        d = 2

    # 범위 초과
    if xx < 0 or yy < 0 or xx >= N or yy >= M:
        check += 1
        continue

    # 이미 방문 or 바다
    if graph[xx][yy] == 1:
        check += 1
    else:
        x = xx
        y = yy
        graph[x][y] = 1
        check = 0
        cnt += 1

    # 뒤쪽으로 이동
    if check == 4:
        if d == 0:  # 북->남
            xx = x + dx[1]
            yy = y + dy[1]
        elif d == 1:  # 동->서
            xx = x + dx[2]
            yy = y + dy[2]
        elif d == 2:  # 남->북
            xx = x + dx[0]
            yy = y + dy[0]
        else:
            xx = x + dx[3]
            yy = y + dy[3]

        if graph[xx][yy] == 1:
            break

print(cnt)

'''
[input]
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

[output]
3
'''
