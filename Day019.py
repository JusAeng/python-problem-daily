h=float(input("Enter high (Metre) : "))
count=0
while h>0.1:
    count+=1
    h*=0.9
    print(f"[#{count}] High : {h:.2f}")
else:
    print("Hit count : {}".format(count))