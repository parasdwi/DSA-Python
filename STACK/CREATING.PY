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

costumstack=stack()
print(costumstack)