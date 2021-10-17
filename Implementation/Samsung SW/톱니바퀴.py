from collections import deque

cycle=[]
cycle.append(deque(list(map(int,input()))))
cycle.append(deque(list(map(int,input()))))
cycle.append(deque(list(map(int,input()))))
cycle.append(deque(list(map(int,input()))))

K=int(input())
List=[]

for _ in range(K):
    List.append(list(map(int,input().split())))

for i in range(K):
    a,b=List[i]
    a=a-1

    cycle_0_1=cycle[0][2]

    cycle_1_0=cycle[1][6]
    cycle_1_2=cycle[1][2]

    cycle_2_1=cycle[2][6]
    cycle_2_3=cycle[2][2]

    cycle_3_2=cycle[3][6]

    #반시계방향
    if b==-1:
        cycle[a].append(cycle[a].popleft())

        #0번(반시계 움직임)과 1번
        if a==0:
            #1번 시계방향으로 이동
            if cycle_0_1!=cycle_1_0:
                cycle[1].appendleft(cycle[1].pop())
                #1번(시계)이 움직여서 2번(반시계)이 움직임
                if cycle_1_2!=cycle_2_1:
                    cycle[2].append(cycle[2].popleft())
                    #2번(반시계)이 움직여서 3번(시계) 움직임
                    if cycle_2_3!=cycle_3_2:
                        cycle[3].appendleft(cycle[3].pop())
        #1번(반시계)와 0번(시계) & 2번(시계)
        elif a==1:
            #0번(시계)
            if cycle_0_1!=cycle_1_0:
                cycle[0].appendleft(cycle[0].pop())
            #2번(시계)
            if cycle_1_2!=cycle_2_1:
                cycle[2].appendleft(cycle[2].pop())

                #3번(반시계)
                if cycle_2_3!=cycle_3_2:
                    cycle[3].append(cycle[3].popleft())

        #2번(반시계)와 1번(시계)&3번(시계)
        elif a==2:
            #1번(시계)
            if cycle_2_1!=cycle_1_2:
                cycle[1].appendleft(cycle[1].pop())
                #0번(반시계)
                if cycle_0_1!=cycle_1_0:
                    cycle[0].append(cycle[0].popleft())

            #3번(시계)
            if cycle_2_3!=cycle_3_2:
                cycle[3].appendleft(cycle[3].pop())


        #3번(반시계)와 2번(시계)
        elif a==3:
            #2번(시계)
            if cycle_3_2!=cycle_2_3:
                cycle[2].appendleft(cycle[2].pop())

                #1번(반시계)
                if cycle_2_1!=cycle_1_2:
                    cycle[1].append(cycle[1].popleft())

                    #0번(시계)
                    if cycle_1_0!=cycle_0_1:
                        cycle[0].appendleft(cycle[0].pop())

    #시계
    elif b == 1:
        cycle[a].appendleft(cycle[a].pop())

        # 0번(시계 움직임)과 1번
        if a == 0:
            # 1번 반시계방향으로 이동
            if cycle_0_1 != cycle_1_0:
                cycle[1].append(cycle[1].popleft())
                # 1번(반시계)이 움직여서 2번(시계)이 움직임
                if cycle_1_2 != cycle_2_1:
                    cycle[2].appendleft(cycle[2].pop())
                    # 2번(시계)이 움직여서 3번(반시계) 움직임
                    if cycle_2_3 != cycle_3_2:
                        cycle[3].append(cycle[3].popleft())
        # 1번(시계)와 0번(반시계) & 2번(반시계)
        elif a == 1:
            # 0번(반시계)
            if cycle_1_0 != cycle_0_1:
                cycle[0].append(cycle[0].popleft())
            # 2번(반시계)
            if cycle_1_2 != cycle_2_1:
                cycle[2].append(cycle[2].popleft())

                # 3번(시계)
                if cycle_2_3 != cycle_3_2:
                    cycle[3].appendleft(cycle[3].pop())

        # 2번(시계)와 1번(반시계)&3번(반시계)
        elif a == 2:
            # 1번(반시계)
            if cycle_2_1 != cycle_1_2:
                cycle[1].append(cycle[1].popleft())
                # 0번(시계)
                if cycle_1_0 != cycle_0_1:
                    cycle[0].appendleft(cycle[0].pop())

            # 3번(반시계)
            if cycle_2_3 != cycle_3_2:
                cycle[3].append(cycle[3].popleft())

        # 3번(시계)와 2번(반시계)
        elif a == 3:
            # 2번(반시계)
            if cycle_3_2 != cycle_2_3:
                cycle[2].append(cycle[2].popleft())

                # 1번(시계)
                if cycle_2_1 != cycle_1_2:
                    cycle[1].appendleft(cycle[1].pop())

                    # 0번(반시계)
                    if cycle_1_0 != cycle_0_1:
                        cycle[0].append(cycle[0].popleft())


result=0

if cycle[0][0]==1:
    result+=1

if cycle[1][0]==1:
    result+=2

if cycle[2][0]==1:
    result+=4

if cycle[3][0]==1:
    result+=8

print(result)
