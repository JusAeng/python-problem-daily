
def modScore(l:list):
    allScore=[]
    with open("Day034.txt","r") as f:
        txt=f.readlines()
        for i in txt:
            temp=i.split()
            allScore.append(temp)
    for j,ele in enumerate(allScore):
        if int(l[0]) >= int(ele[0]):
            allScore.insert(j,l)
            break
    with open("Day034.txt","w") as f:
        nub=0
        for ele in allScore:
            print(ele[0],ele[1],file=f)
            nub+=1
            if nub==5:break

l=[x for x in input("Enter score,name :").split()]
modScore(l)
with open("Day034.txt","r") as f:
    txt=f.readlines()
    for ele in txt:
        print(ele,end="")