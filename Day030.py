n=int(input("Enter Input : "))
ans=n

while ans>0:
    ans-=1
    for i in range(n):
        b=(ans**2-i**2)**(1/2)
        
