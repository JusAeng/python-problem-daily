numbs=[int(x) for x in input("input: ").split()]
print("output:")
ans=[]

for i in range(len(numbs)):
    temp = [x for x in numbs]
    temp.pop(i)
    for j in range(len(temp)):
        ele=temp[j]
        temp.pop(j)
        if sum(temp)==100:
            anslist=[x for x in temp]
            if anslist not in ans:
                ans.append(anslist)
        temp.insert(j,ele)
    
if len(ans)!=0:
    for ele in ans:
        print(ele)
else:
    print("None")