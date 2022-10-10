
def fibo(n):
    assert n>=0 and int(n) ==n, '! N MUST BE POSITIVE INTEGER !'

    if n==0 or n==1:
        return (n)
    else :
        return  fibo(n-1) + fibo(n-2)

l= int(input("ENTER THE LENGTH :"))
for i in range (l):
    print(fibo(i))