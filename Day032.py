def rotateString(s:list,deg:int):
    ans=[]
    for i in range(deg//90):
        for col in range(len(s[0])):
            temp=""
            for row in range(len(s)-1,-1,-1):
                element=s[row][col]
                temp+=element
                # print(element,end="")
            ans.append(temp)
        s.clear()
        for ele in ans:
            s.append(ele)
        ans.clear()
    for ele in s:
        print(ele)
    

deg=int(input("Input Operator:"))
num=int(input("Input num:"))
print("Input String")
s=[input() for x in range(num)]
print("Output:")
error=0

for i in range(1,num):
    if len(s[i])!=len(s[i-1]):
        print("Invalid size")
        error=1
        break
if error!=1:
    rotateString(s,deg)
    