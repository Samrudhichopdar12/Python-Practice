"""dict_1={"juhi":123, "kau": 678, "riya":9807 }
#print(dict_1["kau"])
a=str(input("enter persons name "))
print(dict_1[a])
print(dict_1)"""

"""dict_1={'ram': 1234, 'shyam':678, 'mohan':789 }
dict_1['mohan']=8888
dict_1['raghav']=7878
dict_1['rohan']={'home':4500,'work':99999}
print(dict_1)"""



"""dict_data={1: 'john',2:'jerry',0:'merry'}
#print(dict_data[0])
#del dict_data[2]
#print(dict_data.pop(1))
#print(dict_data)
#dict_data.clear()
#print(dict_data.values())
print(dict_data.items())"""


"""dict_1={1:'diya',2:'john',3:'tim'}
for i in dict_1:
    #print(i)
    print(dict_1[i])"""



"""dict_1={1:'diya',2:'john',3:'tim'}
for i in dict_1.items():
    print(i)    """


"""dict_1={1:'diya',2:'john',3:'tim'}
mydict=dict_1.copy()
print(mydict)"""

dict_1={'child1':{'name':'sunny','age':12}, 'child2':{'name':'jim','age':2} ,'child3':{'name':'tim','age':15}}
"""for x, obj in dict_1.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])"""
for i in dict_1.items():
    print(i)  

print(dict_1['child1']['age'])