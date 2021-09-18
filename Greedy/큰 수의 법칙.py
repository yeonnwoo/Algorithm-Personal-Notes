'''
정당성
: 큰 수로 정렬한 후 큰수의 합의 횟수가 가장 클 때가 가장 큰 합이다.
'''
N,M,K=map(int,input().split())
List=list(map(int,input().split()))

List.sort(reverse=True)
k=0
result=0
for _ in range(M):
    if k==K:
        result+=List[1]
        k=0
    else:
        result+=List[0]
        k+=1

print(result)


'''
[input example]
5 8 3
2 4 5 4 6

[output example]
46


'''
