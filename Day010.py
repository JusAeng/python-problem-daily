mylist=[]
while True:
    a=int(input())
    if a==-1:
        break
    mylist.append(a)
for i in range(len(mylist)):
    count=0
    for j in range(len(mylist)):
        if mylist[i] == mylist[j]:
            count+=1
    if count>len(mylist)/2:
            print(mylist[i])
            break
else:
    print("Not found")