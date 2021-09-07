n=int(input("Enter Input : "))
ans=n
while ans>0:
    ans-=1
    for i in range(2,ans//2):
        b=(ans**2-i**2)**(1/2)
        if b+ans+i==n:
            print(ans)
            ans=0
            break