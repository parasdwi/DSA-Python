def square(a):
    return a*a
def cube(a):
    return a*a*a
funs=[square,cube]
lis=[3,4,9,11,12]
for i in lis:
    var=list(map(lambda x:x(i),funs))
    print(var)