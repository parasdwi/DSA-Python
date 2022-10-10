# SUM_OF_DIGIT_OF_POSITIVE_INT

def sumdigit(n):
    len_n=list(str(n))
    sumd=0
    for i in range(len(len_n)):
        sumd= sumd+n%10
        n=int(n)//10
    return sumd


n= int(input("Enter a positive number :"))
print(sumdigit(n))

       
    