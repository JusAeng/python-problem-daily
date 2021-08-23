import math as m
def factorial(n):
    if n!= 1 and n!=0:
        return n*factorial(n-1)
    return 1
def select(n1,n2):
    return factorial(n1)/(factorial(n2)*factorial(n1-n2))
stair = int(input("Enter number of stair steps : "))
firstSelect=stair//2+1
ans=0
for i in range(m.ceil(stair/2),stair+1):
    firstSelect-=1
    ans+=select(i,firstSelect)
print("when rabbit move 1 or 2 steps in each jump")
print("all posible jumping methods",int(ans))