def isSquare(num:list):
    ansList=[]
    for n in num:
        ans=n**(1/2)-int(n**(1/2))
        if ans == 0:
            ansList.append(int(n))
    ansList.sort()
    return ansList

print(isSquare([1,2,3,4]))
print(isSquare([100,25,36]))
    