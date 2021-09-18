'''
[시간 제한]
1초
O(N^3)으로 해결 가능

[시간 복잡도]
O(N)
'''
s = input()
n = int(s[1])-1  # 행
m = s[0]  # 열
m=ord(m)-97
cnt=0

steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]

for step in steps:
    dx=step[0]
    dy=step[1]
    xx=n+dx
    yy=m+dy

    if xx<0 or yy<0 or xx>=8 or yy>=8:
        continue
    cnt+=1

print(cnt)

'''
[input]
a1

[output]
2
'''
