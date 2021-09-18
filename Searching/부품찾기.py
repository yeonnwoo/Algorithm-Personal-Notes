'''
[시간제한]
- 1초
- N<=1,000,000
- M<=1,000,000

[시간복잡도]

'''
def binary(N, List, target):
    start = 0
    end = N - 1
    while start<=end:
        mid=(start+end)//2

        if List[mid]>target:
            end=mid-1
        elif List[mid]<target:
            start=mid+1
        else:
            return True

    return False

N=int(input())
List=list(map(int,input().split()))
M=int(input())
ans=list(map(int,input().split()))

for i in ans:
    if binary(N,List,i):
        print("yes",end=' ')
    else:
        print("no",end=' ')

'''
[input]
5
8 3 7 9 2
3
5 7 9
'''