
G=int(input())
P=int(input())
dic={}
result=0
visited=set()

for i in range(P):
    g=int(input())
    dic[i]=[j for j in range(1,g+1)]

for key,List in dic.items():
    check=0
    for i in range(len(List)-1,-1,-1):
        if List[i] not in visited:
            result+=1
            check=1
            visited.add(List[i])
            break

    if check==0:
        break

print(result)



'''
[input1]
4
3
4
1
1

[output1]
2

[input2]
4
6
2
2
3
3
4
4

[output2]
3
'''