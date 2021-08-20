def factorial(numb):
    if numb==1 or numb==0:
        return 1
    return numb*factorial(numb-1)
n=int(input("input: "))
print(factorial(n))




 