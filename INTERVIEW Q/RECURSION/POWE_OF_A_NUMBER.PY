def power(n,m):
    assert m>=0 and int(m)==m ,' power must be positive integer'
    if m==0:
        return 1
    else:
        return n*power(n,m-1)

a=int(input('ENTER THE NUMBER :'))
b=int(input('ENTER THE POWER: '))
print(power(a,b))