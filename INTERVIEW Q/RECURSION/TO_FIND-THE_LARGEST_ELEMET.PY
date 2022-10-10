def large(arr,n):
    if n==1 :
        return arr[0]
    else:
        return max(arr[n-1], large(arr,n-1))


a=[1,4,2,9,11,6,7,3]
large(a,len(a))  