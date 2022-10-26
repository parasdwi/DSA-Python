class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
class Singlelinkedlist:
    def __init__(self):
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insert_sll(self,val,loc):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            if loc==0:
                newNode.next=self.head
                self.head=newNode
            else:
                temp=self.head
                index=0
                while index<loc-1:
                    temp=temp.next
                    index+=1
                newNode.next=temp.next
                temp.next=newNode
    def searching(self,val):
        pos=0
        if self.head==None:
            return "can't find"
        else:
            temp=self.head
            while temp!=None:
                if temp.value==val:
                    return pos
                temp=temp.next
                pos+=1
            return 'not in list'
single=Singlelinkedlist()
single.insert_sll(1,0)
single.insert_sll(6,1)
single.insert_sll(1,1)
single.insert_sll(7,1)
single.insert_sll(1,4)
print(single.searching(7))

print([node.value for node in single])