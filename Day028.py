def kumAn(n:int):
    num=str(n)
    digit_list=["","neung","song","sam","si","ha","hok","chet","paet","kao"]
    mul_list=["","sip","roi","pun","meung","san","lan"]
    ans=""
    j=0
    for i in range(len(num),0,-1):
        if num[j]=="0":
            j+=1
            continue
        if j==len(num)-1 and num[j]=="1":
            ans+="et"
        elif j==len(num)-2 and num[j]=="2":
            ans+="yi"+" "
        elif j==len(num)-2 and num[j]=="1":
            None
        else:
            ans+=digit_list[int(num[j])]+" "
        ans+=mul_list[i-1]+" "
        j+=1
    return ans

print(kumAn(int(input("Input Num: "))))
