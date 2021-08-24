def PrimeNumb(N):
    count=0
    for i in range(1,N+1):
        if N%i==0:
            count+=1
    if count!=2:
        return False
    return True
numb=int(input("Input Number: "))
ans=[]
while True:
    numb+=1
    if PrimeNumb(numb)==True:
        if PrimeNumb(numb+2)==True:
            ans.append(numb)
            ans.append(numb+2)
            break
print("next prime number 2step:",ans[0],ans[1])