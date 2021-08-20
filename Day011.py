numb = [int(x) for x in input("enter 2 number: ").split()]
numb.sort()
gcd=1
for i in range(2,numb[0]+1):
    if numb[0]%i ==0 and numb[1]%i==0:
        gcd=i
print("GCD = ",gcd)
