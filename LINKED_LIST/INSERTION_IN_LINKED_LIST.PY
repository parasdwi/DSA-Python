class Node:
    def __init__(self):
        self.values=None
        self.next=None
head=Node()
head=0
temp=Node()
nnode=int(input("ENTER HOW MANY NODES WANT TO ENTER :"))
i=1
val=0
while(i<=nnode):
    val=int(input("Enter the value :"))
    node=Node()
    node.values=val
    node.next=None
    if head==0:
        head=temp=node
    else:
        temp.next=node
        temp=node
    i+=1
temp=head
while(temp!=None):
    print(temp.values,end=' ')
    temp=temp.next