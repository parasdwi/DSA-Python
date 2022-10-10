#captalizeFirst
#Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

#Example

#capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']


def capitalizeFirst(arr):
    newarr=[]
    if len(arr)==0:
        return newarr
    
    newarr.append(arr[0].capitalize())
    return newarr+ capitalizeFirst(arr[1:])

a=['car', 'taco', 'banana']
print(capitalizeFirst(a))