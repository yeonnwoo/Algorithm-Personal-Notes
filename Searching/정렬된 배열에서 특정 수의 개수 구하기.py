from bisect import bisect_left
from bisect import bisect_right

N,x=map(int,input().split())
List=list(map(int,input().split()))

left=bisect_left(List,x)
right=bisect_right(List,x)

if left==right:
    print(-1)
else:
    print(right-left)

'''
[input]
7 2
1 1 2 2 2 2 3

[output]
4
'''