n = int(input())
box=[]
for i in range(n):
    line = input()
    box.append(line)
print()
box.sort()
for i in box:
    print(i)