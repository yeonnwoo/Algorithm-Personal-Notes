'''
정당성
- 매 행의 최소값 중 최대값이 최종적으로 가장 최소 행에서의 최대값이다.
'''

N,M=map(int,input().split())
result=0
Max=0
Min=int(1e9)

for i in range(N):
    temp=list(map(int,input().split()))
    Min=min(temp)

    if Min>Max:
        Max=Min

print(Max)


'''
[input1]
3 3
3 1 2
4 1 4
2 2 2

[output1]
2

[input2]
2 4
7 3 1 8
3 3 3 4

[output2]
3
'''