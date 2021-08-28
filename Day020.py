n=int(input())
list1=[]
list2=[]
for r in range(n):
    a,b=[int(x) for x in input().split()]
    if r%2==0:
        list1.append(a)
        list2.append(b)
    else:
        list1.append(b)
        list2.append(a)
list1.sort()
list2.sort()
s=input()
if s=="Zig-Zag":
    print("Output: {} {}".format(list1[0],list2[-1]))
else:
    print("Output: {} {}".format(list2[0],list1[-1]))




