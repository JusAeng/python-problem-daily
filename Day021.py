def factorial(numb):
    if numb ==1 or numb==0:
        return 1
    elif numb>=2:
        return numb*factorial(numb-1)

n=[int(x) for x in input("input: ").split()]
ans=[]
for ele in n:
    ans.append(factorial(ele))
print("output:",ans)
