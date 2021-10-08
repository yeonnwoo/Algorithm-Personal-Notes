def solution(N, stages):
    result = []
    for i in range(1, N + 1):
        fail_player = len([stage for stage in stages if stage == i])
        success_player = len([stage for stage in stages if stage >= i])

        if success_player == 0:
            result.append((0, i))
        else:
            result.append((fail_player / success_player, i))

    result = sorted(result, key=lambda x: (-x[0], x[1]))

    answer = [result[i][1] for i in range(N)]

    return answer

'''
2019 카카오 기출
'''