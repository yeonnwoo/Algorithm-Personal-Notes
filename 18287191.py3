S=input()
alist=[]
for i in range(26):
    alist.append(-1)
cnt=0
for i in S:
    ind=ord(i)-97
    if alist[ind]==-1: #oo가 중복될때 먼저나온 o 와의 구분을 위해
        del alist[ind]
        alist.insert(ind,cnt) 
    cnt+=1

for i in alist:
    print(i)