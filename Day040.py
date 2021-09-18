s1,s2=[input().lower() for x in range(2)]
s1=s1.replace(" ","")
s2=s2.replace(" ","")
lst1=[x for x in s1]
for j,i in enumerate(s2):
    if i in lst1 and len(s1)==len(s2):
        lst1.remove(i)
    else:
        print("NO")
        break
else: print("YES")