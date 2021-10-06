from collections import deque

N = int(input())
List = list(map(int, input().split()))
List.sort(reverse=True)
que = deque(List)
cnt = 0

while que:
    target = que.popleft()
    for _ in range(target - 1):
        que.pop()
    cnt += 1

print(cnt)

'''
[input]
5
2 3 1 2 2

[output]
2
'''
