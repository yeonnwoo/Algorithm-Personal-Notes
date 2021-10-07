N=int(input())
List=list(map(int,input().split()))
start=0
end=N-1
result=-1

while start<=end:
    mid=(start+end)//2

    if List[mid]<mid:
        start=mid+1
    elif List[mid]>mid:
        end=mid-1
    else:
        result=mid
        break

print(result)


'''
[input]
5
-15 -6 1 3 7

[output]
3
'''