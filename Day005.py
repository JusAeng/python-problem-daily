def checkSame(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i!=j :
                if s[i]==s[j]:
                    return True
    return False
n=input()
print(checkSame(n))