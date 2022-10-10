# lis= ['name',20,19,[2,4],40,'s','py',5]     
lis=[3,4,5,5,2,5,6,5,0]
del lis[0:2]                                # IT CAN DELETE MORE THAN 1 ELEMENT BY SLICING
lis.pop(3)                                  # REQUIRE INDEX TO DELETE ELEMENT FROM BACKWARD
lis.remove(5)                               # IT REQUIRE PERTICULAR ELEMENT YOU WANT TO DELETE
print(lis)