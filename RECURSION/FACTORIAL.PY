def factorial(n):
    assert n>=0 and int(n)== n, '!! N MUST BE POSITIVE INTEGER !!' 
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a= print(factorial(3))
