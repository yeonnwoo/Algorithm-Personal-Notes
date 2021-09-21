'''
[Type 1]. 원래 소수 판별 개선
- 수의 제곱까지만 확인하기
'''
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return "소수가 아닙니다."

    return "소수입니다."


'''
[Type 2]. 에라토스테네스의 체
- 2부터 N까지의 자연수를 나열
- 남은 수 중 아직 처리하지 않은 i의 배수를 모두 제거
'''

#2부터 1000까지 모든 수에 대해 소수 판별
n=1000
List=[1 for _ in range(n+1)]
List[0]=0
List[1]=0

for i in range(2,n+1):
    if List[i]==1:
        for j in range(i*2,n+1,i):
            List[j]=0

#모든 소수 출력
for i in range(2,n+1):
    if List[i]==1:
        print(i,end=' ')