N=int(input())

List=list(map(int,input().split()))
List.sort()

if N%2==0:
    num=N//2-1
else:
    num=N//2

print(List[num])


'''
[input]
4
5 1 7 9

[output]
5
'''