mday=[31,28,31,30,31,30,31,31,30,31,30,31]
mday2=[31,29,31,30,31,30,31,31,30,31,30,31]
d=int(input("Input day: "))
m=int(input("Input month: "))
y=int(input("Input year: "))
nday=d
isLeap=False
if (y-543)%4==0:
    if (y-542)%100 != 0 or (y-543)%400==0:
        isLeap=True
for i in range(m-1):
    if isLeap:
        nday+=mday2[i]
    else: nday+=mday[i]
print("A day of year: {}".format(nday))