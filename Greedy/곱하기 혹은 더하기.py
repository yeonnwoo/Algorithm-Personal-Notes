s=input()
result=0

for data in s:
    if data=='0' or data=='1' or result==0:
        result+=int(data)
    else:
        result*=int(data)

print(result)

'''
[input]
02984

[output]
576
'''