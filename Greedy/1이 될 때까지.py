'''
정당성
- K가 1이 아닌 이상 N을 K로 나눴을 때가 1을 뺐을 때보다 더 빠르게 1로 도달할 수 있다.
- N<=10만
'''

N,K=map(int,input().split())
cnt=0
while True:
    if N==1:
        break

    if N%K==0:
        N=N//K
        cnt+=1
    else:
        N-=1
        cnt+=1

print(cnt)

'''
[input]
25 5

[output]
2
'''