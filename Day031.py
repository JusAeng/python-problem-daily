
def fileTon(n:int):
    if n ==1:
        with open("Ton.txt","r") as f:
            txt=f.read()
            print(txt)
    elif n==2:
        with open("Ton.txt","w") as f:
            print("Write to text : Ton Zan Jus Nut")
            a=["Ton","Zan","Jus","Nut"]
            for ele in a:
                txt=f.write(ele)
    elif n==3:
        with open("Ton.txt","a") as f:
            a=["Computer","Engineering"]
            print("Update to Text : Computer Engineering")
            for ele in a:
                f.write(ele)
    
fileTon(int(input("Enter num 1 or 2 or 3 : ")))

