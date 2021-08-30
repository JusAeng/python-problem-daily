snum=input()
sumoff=0
pos=10
for ele in snum:
    sumoff+=(int(ele)*pos)
    pos-=1
ans=sumoff%11
if ans==0:
    snum+="0"
else:
    snum+=str(11-ans)
print(snum)