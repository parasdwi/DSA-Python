def insertionsort(lis):
    for i in range(1,len(lis)):
        key=lis[i]
        j=i-1
        while j>=0 and key<lis[j]:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=key
    return lis

lis=[3,5,2,1,6,0,9,11,4,10]
print(insertionsort(lis))