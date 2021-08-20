s= input()
checkLists=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(s)):
    checkLists[int(s[i])]=100
checkLists.sort()
for i in range(len(s)):
    checkLists.pop()
if len(checkLists)==0:
    print("None")
else:
    ans=" ".join([str(x) for x in checkLists])
    print(ans)
