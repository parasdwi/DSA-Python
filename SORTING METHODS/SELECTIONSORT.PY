def selectionsort(lis):
    for i in range(len(lis)):
        minimum= i
        for j in range(i+1,len(lis)):
            if lis[minimum]> lis[j]:
                minimum=j
        lis[i],lis[minimum]=lis[minimum],lis[i]
    return lis

lis=[4,5,2,0,3,9,1]
print(selectionsort(lis))
