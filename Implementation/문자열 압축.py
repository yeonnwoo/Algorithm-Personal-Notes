from collections import deque

def solution(s):
    Min = len(s)
    que = deque()

    for i in range(1, len(s) // 2 + 1):
        result = ''
        que.clear()
        for j in range(0, len(s), i):
            temp = s[j:j + i]
            if len(que) == 0:
                que.append(temp)
            else:
                target = que[-1]
                if temp == target:
                    que.append(temp)

                else:
                    if len(que) != 1:
                        result += str(len(que))
                        result += que.pop()
                    else:
                        result += que.pop()

                    que.clear()
                    que.append(temp)

        if len(que) != 1:
            result += str(len(que))
            result += que.pop()
        else:
            result += que.pop()

        if len(result) < Min:
            Min = len(result)

    return Min

'''
2020 카카오 신입공채 기출
'''