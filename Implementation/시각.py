'''
[시간제한]
N<=23, 2초
O(N^3)*2 로 해결가능

[시간 복잡도]
O(N^3)
'''

N=int(input())
cnt=0

for i in range(N+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1

print(cnt)

'''
[input]
5

[output]
11475
'''