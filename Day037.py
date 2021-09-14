class SinglyLinkedListNoDummy :

    class Node:                                 #collect data
        def __init__(self,data,next=None):
            self.data=data
            if next == None:
                self.next=None
            else:
                self.next=next
    def __init__(self):
        self.head= None
        self.tail=None
        self.size= 0
    def __str__(self) -> str:                   #ele in linked list
        s='linked data'
        p=self.head
        while p!= None:
            s+=str(p.data)
            p = p.next
        return s
    
    def __len__(self):                          #เพิ่มเมื่อเติม ลดเมื่อเอาออก
        return self.size
    def isEmpty(self):
        return self.size == 0
    def indexOf(self,data):
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p=p.next
        return -1
    def isIn(self,data):                        #check if data in linked list
        return self.indexOf(data) >= 0
    def nodeAt(self,i):                         #find node at index i
        p=self.head
        for j in range(0,i):
            p= p.next
        return p
    def append(self,data):                          #add node at last
        if self.head is None :
            p=self.Node(data)
            self.head=p
            self.tail=p
            self.size+=1
        else:
            self.insertAfter(len(self)-1,data)

    def insertAfter(self,i,data):                  #insert sequence in linked list
        q = self.nodeAt(i)
        p = self.Node(data)
        if q == self.tail:
            self.tail=p
        p.next = q.next
        q.next = p
        self.size+=1
    def addTail(self,data):
        q = self.tail
        p= self.node(data)
        q.next = p
        self.tail = p
        self.size +=1

    def removeTail(self):
        if self.size > 0:
            q=self.nodeAt(len(self)-2)
            self.tail = q
            q.next = None
    def deleteAfter(self,i):
        if self.size > 0:
            q= self.nodeAt(i)
            if i == len(self)-2:
                self.tail = q
            q.next = q.next.next
        self.size-=1
    def delete(self,i):
        if i == 0 and self.size >0:                     #delete first ele
            self.head = self.head.next
            self.size-=1
        else: 
            self.deleteAfter(i-1)
    def removeData(self,data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)
    def addHead(self,data) :
        if self.isEmpty():
            p=self.Node(data)
            self.head = p
            self.size+=1
        else:
            p = self.Node(data,self.head)
            self.head= p
            self.size+=1