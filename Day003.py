list1=[]
while True:
    x = int(input())
    list1.append(x)
    if x==0 :
        break
s=input()
if s.lower()=="min":
    list1.sort()
else :
    list1.sort()
    list1.reverse()
ans = " ".join([str(x) for x in list1])
print(ans)

