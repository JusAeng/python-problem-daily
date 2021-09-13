print("Input:")
conclu=""
player1,player2=0,0
m=int(input())
for i in range(3*m):
    p1,p2=input().split()
    if p1==p2:
        None
    elif (p1=="R" and p2=="S") or (p1=="S" and p2=="P") or (p1=="P" and p2=="R"):
        player1+=1
    else:
        player2+=1
    
    if player1==m or player2==m:
        if player1==m: conclu="Player 1 wins"
        else: conclu="Player 2 wins"
        break

else:
    conclu="Tie"

print("Output:")
print(player1,player2)
print(conclu)