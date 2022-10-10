from array import *

# BY USING ITRATION

def searching(arr,n):
    for i in range(len(arr)):
        if arr[i]== n:
            return i+1
        elif  len(arr)==i+1:
            return 'number not in arr'

# BY USING RECURRSION

def searching2(arr,n):
    if arr[0]==n:
        return 1
    if len(arr)==1:
        return 2
    return 1 + searching2(arr[1:],n)

arr= array('i', [3,5,6,2,9,10])
ans=searching2(arr,5)
if ans>=len(arr):
    print('not in array')
else:
    print(ans)
