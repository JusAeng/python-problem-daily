class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
class SinglyLinkedList:
        def __init__(self) :
            self.head=None
            self.tail=None

        def __str__(self):
            node = self.head
            ans = []
            while node:
                ans.append(str(node.value))
                node = node.next
            if ans == []:
                return "Empty"
            return "->".join(ans)

        def size(self):
            p=self.head
            i=0
            while p:
                i+=1
                p=p.next
            return i
        def indexOf(self,value):
            p=self.head
            i=0
            while p:
                if p.value==value:
                    return i
                i+=1
                p=p.next
            return -1
        def nodeAt(self,i):
            p=self.head
            for j in range(i):
                p=p.next
            return p
        def dataAt(self,i):
            return self.nodeAt(i).value

        def append(self,value):
            node=Node(value)
            if self.head==None:
                self.head=node
                self.tail=node
            else:
                p=self.tail
                p.next=node
                self.tail=node
        def addHead(self,value):
            if self.size()==0:
                self.append(value)
            else:
                node=Node(value)
                p=self.head
                node.next=p
                self.head=node
        def deleteHead(self):
            if self.size()==1:
                pick=self.head.value
                self.head=None
                self.tail=None
                return pick
            elif self.size()>1:
                p=self.head
                pick=p.value
                n=p.next
                self.head=n
                return pick
        def deleteTail(self):
            if self.size()==1:
                return self.deleteHead()
            elif self.size()>1:
                p=self.tail
                pick=p.value
                n=self.nodeAt(self.indexOf(p.value)-1)
                n.next=None
                self.tail=n
                return pick
        
        def pop(self,i=None):
            if i==None or i==self.size()-1:
                return self.deleteTail()
            elif 0<i<self.size():
                p=self.nodeAt(i)
                before=self.nodeAt(i-1)
                before.next=p.next
                return p.value
            elif i==0:
                return self.deleteHead()
        def insert(self,i,value):
            if i==0:
                self.addHead(value)
                print("eiei")
            elif i==self.size():
                self.append(value)
            elif 0<i<self.size():
                before=self.nodeAt(i-1)
                n=Node(value)
                n.next=before.next
                before.next=n
        def insertAfter(self,i,value):
            self.insert(i+1,value)

# link_1=SinglyLinkedList()
# for i in range(10):
#     link_1.append(i+1)
# link_1.addHead(4)
# print(link_1)