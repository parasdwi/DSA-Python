# COPY METHOD
dic={'name':'Paras','Age': 24,'Crush': 'Nandu','address':'BHARTHANA','Status':'Single'}
dic2=dic.copy()
print(dic2)

# from key method
newdic={}.fromkeys([1,2,3],9)
print(newdic)
newdic={}.fromkeys([1,2,3])
print(newdic)

# get method
print(dic.get('Age'))
print(dic.get('city','etawah'))
print(dic)

# items method
print(dic.items())      # returns the list of tuple of key, value pair

# key method
print(dic.keys())       # return the list of keys

# setdefault method
print(dic.setdefault('name1','added'))
print(dic)

# vallues method
print(dic.values())      # return the list of values

# update method (it takes the dictionary or a tuple as parameter)
dic.update(newdic)
print(dic)

