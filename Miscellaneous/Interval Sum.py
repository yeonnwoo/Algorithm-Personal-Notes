'''
Prefix Sum
'''

n=5
data=[10,20,30,40,50]

#prefix Sum 계산
Sum=0
pre=[0]

for i in data:
    Sum+=i
    pre.append(Sum)

#구간합
left=3
right=4

print(pre[right]-pre[left-1])

