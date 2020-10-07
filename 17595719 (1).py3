N=int(input())
k=N
cnt=0
    
while True:
    cnt=cnt+1
    a=k//10
    b=k%10
    new=a+b
    ans=b*10+new%10
    k=ans
    if ans==N:
        break
        
                           
print(cnt)  