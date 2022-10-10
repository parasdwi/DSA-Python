

class stack():
    def __init__(self):
        self.list=["w","d","o","i","p","n"]
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            return "CAN'T PERFORM POP Operation"
        else:
            return self.list.pop()
    def push(self,value):
        return self.list.append(value)
    
    def peek(self):
        if self.isempty():
            return "CAN'T PERFORM POP Operation"
        return self.list[len(self.list)-1]
    
costumstack=stack()
# print(costumstack)
print(costumstack.pop())
# print(costumstack)
print(costumstack.peek())

