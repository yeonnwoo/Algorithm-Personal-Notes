from collections import deque

# 오른쪽,아래,왼쪽,위
dic = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0]
}

N = int(input())
K = int(input())  # 사과개수
apple = []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a - 1, b - 1))

# 방향정보
L = int(input())
Time = []
direct = []
for _ in range(L):
    a, b = map(str,input().split())
    Time.append(int(a))  # a초 뒤
    direct.append(b)  # 방향

cnt = 0
tail_x = 0
tail_y = 0
head_x = 0
head_y = 0
now_dir = 0  # 현재는 오른쪽 방향
dragon = deque()
dragon.append((0, 0))

while True:
    if cnt in Time:
        D=direct.pop(0)

        if D=='L':
            if now_dir==0:
                now_dir=3
            elif now_dir==1:
                now_dir=0
            elif now_dir==2:
                now_dir=1
            else:
                now_dir=2
        else:
            if now_dir==0:
                now_dir=1
            elif now_dir==1:
                now_dir=2
            elif now_dir==2:
                now_dir=3
            else:
                now_dir=0

    # 머리 늘림
    dx, dy = dic[now_dir]
    head_x += dx
    head_y += dy

    # 벽에 부딪힘
    if head_x < 0 or head_y < 0 or head_x >= N or head_y >= N:
        break

    # 자기자신과 부딪힘
    if (head_x, head_y) in dragon:
        break

    dragon.appendleft((head_x, head_y))

    # 사과가 없음
    if (head_x, head_y) not in apple:
        tail_x += dx
        tail_y += dy
        dragon.pop()
    else:
        apple.remove((head_x,head_y))

    cnt += 1

print(cnt+1)
