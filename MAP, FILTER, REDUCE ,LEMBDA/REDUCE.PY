from functools import reduce

lis=[4,5,1,0,9,8]
var=reduce(lambda x,y:x+y,lis)
print(var)