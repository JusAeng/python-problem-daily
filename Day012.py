n=int(input())
input1=[]
for i in range(n):
    input1.append(int(input()))
input2 = [int(x) for x in input().split()]
input3=[]
while True:
    input3.append(int(input()))
    if input3[-1]==-1:
        input3.pop()
        break
logic=0
ans=[]
for numb in input1+input2+input3:
    if logic == 0:
        ans.append(numb)
        logic=1
    else:
        ans.insert(0,numb)
        logic=0    
print(ans)
    


    
