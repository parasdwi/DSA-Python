def bubblesort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j+1],lis[j]=lis[j],lis[j+1]
    return lis

lis=[4,5,2,0,3,9,1]
print(bubblesort(lis))
