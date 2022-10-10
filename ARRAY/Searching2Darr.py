import numpy as np

def searching2D(arr,n):
    c=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]==n:
                print (i+1,j+1)
                c+=1
    if c==0:
        print('Element not in array')

arr=np.array([[2,3,4,5],[6,7,2,1],[10,12,3,4],[0,5,9,12]])
searching2D(arr,22)

