def PrimeNumb(N):
    count=0
    for i in range(1,N+1):
        if N%i==0:
            count+=1
    if count!=2:
        return False
    return True

n=int(input())
while True:
    n+=1
    if PrimeNumb(n)==True:
        break
print(n)






