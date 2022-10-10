def quicksort(arr,l,e):
    if (l<e):
        i=l
        j= len(arr)-1
        pivot=l
        while i<j:
            while arr[i]<=arr[pivot] and i<e:
                i+=1
            while arr[j]>arr[pivot]:
                j-=1
            if i<j:
                arr[j],arr[i]=arr[i],arr[j]
        arr[j],arr[pivot]=arr[pivot],arr[j]
        quicksort(arr,l,j-1)
        quicksort(arr,j+1,e)
    return arr

arr=[0,9,1,10,4,11,5,3]
print(quicksort(arr,0,len(arr)-1))

        