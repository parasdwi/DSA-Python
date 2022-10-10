import numpy as np

arr=np.array([[2,3,4,5],[6,7,2,1],[10,12,3,4],[0,5,9,12]])
newarr= np.delete(arr,0,axis=0)       # delete row of index 0
newarr= np.delete(arr,0,axis=1)       # delete column of index 0

print(newarr)