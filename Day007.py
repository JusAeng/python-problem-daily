v1=[float(x) for x in input().split()]
v2=[float(x) for x in input().split()]
Multi=[]

if len(v1) == len(v2):
    for i in range(len(v1)):
        Multi.append(v1[i]*v2[i])
    print(sum(Multi))
else:
    print("Error")


