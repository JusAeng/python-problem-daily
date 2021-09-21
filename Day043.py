import numpy as np
n=int(input())
S=[]
for i in range(n):
    S.append([int(x) for x in input().split()])
W=[float(x) for x in input().split()]

S=np.array(S)
W=np.array(W)
for i in range(n):
    print(S[i].dot(W))