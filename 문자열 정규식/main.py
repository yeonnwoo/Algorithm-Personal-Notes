import re

s=input()

p=re.compile('pi|ka|chu')

List=p.findall(s)

ans=''.join(s)

if s==ans and len(List)!=0:
    print('YES')
else:
    print('NO')
