def C(n,k):
    if 0<k<n:
        return C(n-1,k)+C(n-1,k-1)
    elif k==0 or n==k:
        return 1
    else: return 0


n,k=[int(input()) for x in range(2)]
print(C(n,k))