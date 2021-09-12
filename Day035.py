n=int(input())
lst_set=[set(int(y) for y in input().split()) for x in range(n)]

u=set()
isec=set(lst_set[0])
for i in range(len(lst_set)):
    u=u.union(lst_set[i])
    isec=isec.intersection(lst_set[i])
print(len(u))
print(len(isec))