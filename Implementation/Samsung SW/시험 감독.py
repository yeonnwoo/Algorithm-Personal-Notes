import math

N=int(input())
people=list(map(int,input().split()))
B,C=map(int,input().split())
cnt=0
for val in people:
    val=val-B
    cnt+=1
    if val>0:
        cnt+=math.ceil(val/C)

print(cnt)

