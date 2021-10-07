S=input()
num=0
result=[]

for data in S:
    if data.isdigit():
        num+=int(data)
    else:
        result.append(data)

result.sort()

print(''.join(result)+str(num))
        

'''
[input]
K1KA5CB7

[output]
ABCKK13
'''