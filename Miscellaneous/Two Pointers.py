'''
특정한 합을 가지는 부분 연속 수열 찾기
- 음수 데이터가 없는 경우
'''

def Two_Pointer_ver1(data, m):
    start = 0
    end = 0
    cnt = 0
    Sum = data[0]

    while start <= end < len(data):
        if Sum < m:
            end += 1
            Sum += data[end]

        elif Sum > m:
            Sum -= data[start]
            start += 1

        else:
            cnt += 1
            Sum -= data[start]
            start += 1

    print(cnt)


def Two_Pointer_ver2(data, m):
    end = 0
    cnt = 0
    Sum = 0

    # start를 증가시키며 반복
    for start in range(len(data)):
        # end를 가능한 만큼 이동
        while Sum < m and end < len(data):
            Sum += data[end]
            end += 1

        if Sum == m:
            cnt += 1

        Sum -= data[start]

    print(cnt)


data = [1, 2, 3, 2, 5]
m = 5

Two_Pointer_ver1(data, m)
Two_Pointer_ver2(data, m)


'''
[1,2,3,2,5]의 부분합이 5인 경우의 수
'''

