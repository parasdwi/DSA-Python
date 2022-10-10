from array import *
arr1=array('i',[5,6,3,9,1])

arr1.insert(5,0)          # time complexity O(1)
arr1.insert(0,0)          # time complexity O(n)
arr1.insert(3,10)         # time complexity O(n)
print(arr1)