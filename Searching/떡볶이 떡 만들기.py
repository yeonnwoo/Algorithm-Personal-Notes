'''
[시간제한]
2초
N<1,000,000
M<2,000,000,000

변수 x : 절단된 후 남은 길이

'''
N,target=map(int,input().split())
List=list(map(int,input().split()))
result=0
start=0
end=max(List)

while start<=end:
    mid=(start+end)//2
    Sum=0

    for data in List:
        if data>mid:
            Sum+=data-mid

    if Sum<target:
        end=mid-1

    else:
        result=mid
        start=mid+1

print(result)


'''
[input]
4 6
19 15 10 17

[output]
15
'''