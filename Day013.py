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
list1,list2=[1,2,3,4],[1,4,3,4,5,2]
print(c_subset(list1,list2))