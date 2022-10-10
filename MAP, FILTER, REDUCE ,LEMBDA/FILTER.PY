def number_greater_than_5(x):
    if x>5:
        return x

lis=[4,2,6,22,0,21,8,5,9]
var=list(filter(number_greater_than_5,lis))
print(var)