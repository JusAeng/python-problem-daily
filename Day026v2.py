from time import time
p1,p2,p3,n1,n2 = [int(x) for x in input().split()]
start = time()
bonus=0

for i in range(n1,n2+1):
    if i ==p1:
        bonus+=10000
    if i%100 == p2:
        bonus+=25
    if i%1000 == p3:
        bonus+=100

print(bonus)
print(f'Time taken to run: {time() - start} seconds')