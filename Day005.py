def c_duplicate(numb):
    numb=str(numb)
    for enumb in numb:
        count=0
        for i in range(len(numb)):
            if enumb == numb[i]:
                count+=1
            if count >1:
                return True
    return False
numb = int(input("input: "))
print(c_duplicate(numb))
