def mod_duplicate(list1):
    copyList=[]
    for elist1 in list1:
        if elist1 not in copyList:
            copyList.append(elist1)
    return copyList
def c_subset(list1,list2):
    mod_duplicate(list1)
    mod_duplicate(list2)
    count=0
    for elist1 in list1:
        for i in range(len(list2)):
            if elist1==list2[i]:
                count+=1
                break
    if count==len(list1) or count>=len(list2):
        return True
    return False
line=[x for x in input().split("],[")]
list1=list(int(x) for x in line[0][1:].split(","))
list2=list(int(x) for x in line[1][0:-1].split(","))
print(c_subset(list1,list2))

# [1,2,3,4,5,6],[1,2]


