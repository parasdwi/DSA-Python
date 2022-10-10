# ALL operation (if all KEYS in dict are true or empty then it return true)

from multiprocessing.sharedctypes import Value


dic1={}
dic2={0:True, 1:True}
print(all(dic1))
print(all(dic2))

# ANY operation (if ANY KEYS in dict IS true or empty then it return true)

print(any(dic2))
print(any(dic2))

# SORTED operation ( it sorts the key and return in list we can reverse the list or sort on the base of length of key)

dic3={'f':5,'b':9,'a':0,'nb':1,'da':11}
print(sorted(dic3,reverse=True,key=len))
