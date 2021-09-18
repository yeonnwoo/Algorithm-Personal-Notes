'''
[시간제한]
이동횟수<=100
O(N^3)까지 가능

[시간 복잡도]
O(N)
'''
N = int(input())
List = list(map(str, input().split()))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 0
y = 0
xx = 0
yy = 0

for direct in List:
    if direct == 'U':
        xx = x + dx[0]
        yy = y + dy[0]

    elif direct == 'D':
        xx = x + dx[1]
        yy = y + dy[1]

    elif direct == 'L':
        xx = x + dx[2]
        yy = y + dy[2]

    elif direct == 'R':
        xx = x + dx[3]
        yy = y + dy[3]

    if xx < 0 or yy < 0 or xx >= len(List) or yy >= len(List):
        continue
    x = xx
    y = yy

print(x + 1, y + 1)

'''
[input]
5
R R R U D D

[output]
3 4
'''
