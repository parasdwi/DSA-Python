import math as m

def insertionsort(lis):
    for i in range(1,len(lis)):
        key=lis[i]
        j=i-1
        while j>=0 and key<lis[j]:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=key
    return lis

def bucketsort(carr):
    buckets= round(m.sqrt(len(carr)))
    maxelement=max(carr)
    arr=[]
    for i in range(buckets):
        arr.append([])
    for j in carr:
        ind= m.ceil(j*buckets/maxelement)
        arr[ind-1].append(j)
    for i in range(buckets):
        arr[i]=insertionsort(arr[i])
    k=0
    for i in range(buckets):
        for j in range(len(arr[i])):
            carr[k]=arr[i][j]
            k+=1
    return carr


lis=[3,5,2,1,6,0,9,11,4,10]
print(bucketsort(lis))    