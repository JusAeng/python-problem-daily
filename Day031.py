
def fileTon(n:int):
    if n ==1:
        with open("Ton.txt","r") as f:
            txt=f.read()
            print(txt)
    elif n==2:
        with open("Ton.txt","w") as f:
            new=input("Write to text : ")
            new=new.split()
            for ele in new:
                txt=f.write(ele)
    elif n==3:
        with open("Ton.txt","a") as f:
            update=input("Update to Text : ")
            update=update.split()
            for ele in update:
                f.write(ele)
    
fileTon(int(input("Enter num 1 or 2 or 3 : ")))

