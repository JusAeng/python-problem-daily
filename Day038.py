class Student:
    def __init__(self,ids,score) -> None:
        self.ids=ids
        self.score=score
        self.rank=None
    def __str__(self) -> str:
        return "{},{}".format(self.ids,self.score)
    def setRank(self,rank):
        self.rank=rank
    def getRank(self):
        return self.rank
    def getScore(self):
        return self.score
    def getID(self):
        return self.ids

room=[]
find=0
while True:
    temp=[float(x) for x in input().split()]
    if len(temp)==2:
        temp_st=Student(int(temp[0]),temp[1])
        room.append(temp_st)
    else: 
        find=int(temp[0])
        break

lst_score=[]
lst_id=[]
for student in room:
    lst_id.append(student.getID())
    lst_score.append(student.getScore())

lst_score.sort()
lst_score.reverse()
lst_id.sort()
# print(lst_id)
# print(lst_score)

rank_run=1
for sc in lst_score:
    for student in room:
        if student.getScore()==sc and student.getRank()==None:
            student.setRank(rank_run)
            rank_run+=1
            break

for student in room:
    if student.getID()==find:
        print(student.getRank())
        break
else:
    print("Not Found")
