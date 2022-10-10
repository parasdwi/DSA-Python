# SUM_OF_DIGIT_OF_POSITIVE_INT

def sumdigit(n):
    assert n>=0 and int(n)==n ,' N MUST BE POSITIVE INTEGER'
    if n==0:
        return 0
    else: 
       return n%10+sumdigit(n//10)


n= int(input("Enter a positive number :"))
print(sumdigit(n))