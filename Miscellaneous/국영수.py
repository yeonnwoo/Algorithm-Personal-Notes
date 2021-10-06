N=int(input())
student=[]

for _ in range(N):
    student.append(list(map(str,input().split())))

student=sorted(student,key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in student:
    print(i[0])

'''
[input]
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

[output]
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan

'''