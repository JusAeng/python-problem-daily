a=int(input("InputA: "))
count=0
while count<5:
    b=int(input("InputB: "))
    if b>a:
        print("Higher")
    elif b<a:
        print("Lower")
    else:
        print("You win")
        break
    count+=1
else:
    print("You Lose")

