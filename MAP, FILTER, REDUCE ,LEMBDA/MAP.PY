a='paras dwivedi'
b=a.split()
c=''
for i in b:
    c=c+' '+i.capitalize()
print(c[1:])

#or 
b=list(map(lambda x:x.capitalize(),b))
a=' '.join(b)
print(a)