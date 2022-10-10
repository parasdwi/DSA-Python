#

def issu():
    return isal()
    print('issu')
def isal():
    mam()
    print('isal')
def mam():
    print('mam')

a=[3,4,5]
b=[6,4,8]
a.extend(b)
print(a)

def flatten(arr):
    arr1=[]
    for i in arr:
        if type(i) is list:
            arr1.extend(flatten(i))
        else:
            arr1.append(i)
    return arr1

a=[3,4,9,1,[4,7,0,2,[5,6]]]
flatten(a)

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}


def nestedeven(obj,sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum+= nestedeven(obj[i])
        elif obj[key] is int and obj[key]%2==0:
            sum+= obj[key]
    return sum

nestedeven(obj1)
        
