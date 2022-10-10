import numpy as np

arr = np.array([[2, 3, 4, 5], [6, 7, 2, 1], [10, 12, 3, 4], [0, 5, 9, 12]])
print(arr)

newarr = np.insert(arr, 0, [44, 55, 66, 77], axis=1)
print(newarr)

newarr2 = np.insert(arr, 2, [44, 55, 66, 77], axis=0)
print(newarr2)

newarr3 = np.append(newarr, [[11, 22, 33, 44,55]], axis=0)
print(newarr3)
