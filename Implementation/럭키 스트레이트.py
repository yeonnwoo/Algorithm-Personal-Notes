N=str(int(input()))
n=len(N)//2
left=N[:n]
right=N[n:]
left_sum=0
right_sum=0

for s in range(n):
    left_sum+=int(left[s])
    right_sum+=int(right[s])

if left_sum==right_sum:
    print("LUCKY")

else:
    print("READY")