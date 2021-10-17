from itertools import permutations
import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip().split()))
List = list(map(int, sys.stdin.readline().strip().split()))
cur = ['+'] * List[0] + ['-'] * List[1] + ['*'] * List[2] + ['%'] * List[3]

pro = set(permutations(cur))
Max = -10**9
Min = 10**9

for List in pro:
    result = num[0]
    for i in range(1, N):
        val = num[i]
        cal = List[i - 1]

        if cal == '+':
            result += val
        elif cal == '-':
            result -= val
        elif cal == '*':
            result *= val
        else:
            result=int(result/val)

    if Max < result:
        Max = result
    elif Min > result:
        Min = result

    if Max == -10 ** 9:
        Max = result
    if Min == 10 ** 9:
        Min = result

print(Max)
print(Min)