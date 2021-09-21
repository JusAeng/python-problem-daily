def sumlist(x:list):
    ans=0
    for e in x:
        if e==[]:
            ans=0
        elif type(e)==list:
            ans+=sumlist(e)
        else:
            ans+=e
    return ans
    
print(eval(input().strip()))