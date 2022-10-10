from array import *
# IT DO NO WORK FOR REPEATED ELEMENTS
def deleating(arr,n):
    c=0
    for i in range(len(arr)):
        if arr[i]==n:
            c+=1
            for j in range(i,len(arr)-c):
                arr[j]=arr[j+1]

        if len(arr)==i:
            return 'NUMBER NOT PRESENT IN ARRAY'
    return arr[:len(arr)-c]
        
a1= array('i',[3,9,7,1,0,9,5,0,11,5])
print(deleating(a1,9))
