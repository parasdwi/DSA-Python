class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class creation:
    def __init__(self):
        self.head=None
        self.tail=None
    
singlelinkedlist=creation()
node1=Node(1)
node2=Node(2)
singlelinkedlist.head=node1
singlelinkedlist.head.next=node2
singlelinkedlist.tail=node2
print(node1.value)
print(node2.next)