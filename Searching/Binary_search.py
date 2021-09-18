def binary_search(array,target,start,end):

    while start<=end:
        mid=(start+end)//2

        if array[mid]<target:
            start=mid+1
        elif array[mid]>target:
            end=mid-1
        else:
            return mid
    return None

# 원소의 개수,찾고자하는 문자열
n,target=list(map(int,input().split()))

#전체 문자열
array=list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result=binary_search(array,target,0,n-1)
if result==None:
    print("해당 원소가 존재하지 않습니다.")
else:
    print(result+1)

'''
[input]
10 7
1 3 5 7 9 11 13 15 17 19

[output]
4
'''