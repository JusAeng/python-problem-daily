p1,p2,p3,n1,n2 = [int(x) for x in input().split()]
bonus=0

#5digit
if n1<=p1<=n2:
    bonus+=10000

#3digit
r3=n2//1000-n1//1000
win3=(r3-1)
if n1%1000<=p3:
    win3+=1
if n2%1000>=p3:
    win3+=1
bonus+=win3*100

#2digit
r2=n2//100-n1//100
win2=(r2-1)
if n1%100 <= p2:
    win2+=1
if n2%100 >= p2:
    win2+=1
bonus+=win2*25

print(bonus)