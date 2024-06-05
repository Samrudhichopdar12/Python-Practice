"""tuple_1=("apple","banana","cherry")
print(tuple_1)
print(len(tuple_1))
print(type(tuple_1))"""


"""#use a tuple() constructor to make a tuple
thistuple = tuple(("apple","mango","cherry"))
print(thistuple)"""


"""my_tuple=("apple",1,2,3,'True')
print(my_tuple[0])
print(my_tuple[-2])
print(my_tuple[1:5])
print(my_tuple[:4])
print(my_tuple[2:])"""


"""#to check if apple is present in tuple
my_tuple=("apple",1,2,3,'True')

if "apple" in my_tuple:
    print("\n apple is present in tuple")"""


"""my_tuple=("apple",1,2,3,'True')
my_list=list(my_tuple)  
print(my_list) 

my_list[0]="mango"
print(my_list)"""

"""thislist=("apple","pineapple","cherry")
mylist=("orange",)
thislist += mylist
print(thislist)"""


#use of for loop
"""my_list=("apple","kiwi","papaya","cherry")
for i in my_list:
    print(i)"""

"""for i in range(len(my_list)):
    print(my_list[i])  """  

#use of while loop
"""my_list=("apple","kiwi","papaya","cherry")
i=0
while i< len(my_list):
    print(my_list[i])
    i=i+1    """

tuple1=(1,3,4,'car',8,9)
tuple2=(5,6,7,"apple")
tuple3=tuple1+tuple2
x=tuple3*2
print(x)   