from collections import deque
from collections import Counter
import sys

def is_break(List):
    if 0 in dict(Counter(List)).keys():
        if dict(Counter(List))[0] >= K:
            return True

    return False

N,K=map(int,sys.stdin.readline().strip().split())

#내구도
List=list(map(int,sys.stdin.readline().strip().split()))
step=0

#컨베이어 벨트
up=deque([i for i in range(N)])
down=deque([i for i in range(2*N-1,N-1,-1)])

#로봇의 위치
robot=deque()

while True:
    step += 1
    '''
    벨트 회전
    '''
    u=up.pop()
    d=down.popleft()

    up.appendleft(d)
    down.append(u)

    #로봇이 내리는 위치에 오면 바로 내림
    if up[-1] in robot:
        robot.remove(up[-1])

    '''
    로봇 이동
    '''
    n=len(robot)
    temp_que=deque()
    for _ in range(n):
        r=robot.popleft()

        uu=up.index(r) #로봇이 있는 위치에서 up의 인덱스
        next_num=up[uu+1] #그 다음 컨베이어 벨트 숫자

        #그 다음의 내구성이 1 이상이고 로봇이 없음
        if List[next_num]>=1 and next_num not in robot and next_num not in temp_que:
            #이동(제일 처음 올라간 애니까 제일 처음에 append)
            temp_que.append(next_num)

            #내구성 감소
            List[next_num]-=1

        #못 움직임
        else:
            temp_que.append(r)

    robot=temp_que

    if is_break(List):
        break

    # 로봇이 내리는 위치에 오면 바로 내림
    if up[-1] in robot:
        robot.remove(up[-1])

    '''
    로봇 올림
    '''

    if List[up[0]]!=0:
        robot.append(up[0])

        #내구성 감소
        List[up[0]]-=1

    if is_break(List):
        break

print(step)