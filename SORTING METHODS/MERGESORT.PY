def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = []
    R = []

    for i in range(n1):
        L.append(customList[l+i])
    
    for j in range(n2):
        R.append(customList[m+1+j])
    
    i = 0 
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l+r)//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList


arr=[3,2,6,1,7,11]
print(mergeSort(arr,0,len(arr)-1))
