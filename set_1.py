"""set_1={"apple",1,2,4.5,"john"}
print(set_1)
print(len(set_1))
print(type(set_1))"""

#using set() constructor
"""my_set=set(("apple",1,2,4.5,"john"))
print(my_set)"""


#use of for loop
"""set_1={"apple",1,2,4.5,"john"}

for i in set_1:
    print(i)"""

#to check 1 is present
"""if 1 in set_1:
    print("\n 1 is present in set ")"""

#add lemon to set
"""set_1={"mango","papaya","kiwi"}
set_1.add("lemon")
print(set_1)  """

#add elements from myset to thisset

"""thisset={"pink","yellow","blue"}
myset={"green","black"}

thisset.update(myset)
print(thisset)"""

#add list elements to set
"""my_set={"apple","cherry","coconut"}
my_list=["papaya","lemon"]

my_set.update(my_list)
print(my_set)"""

#remove and pop
"""set_1={"apple",1,2,4.5,"john"}

set_1.remove("apple")
print(set_1.pop())
print(set_1)"""

"""set_1.clear()
print(set_1)"""

#join  sets

"""set1={1,2,3,4}
set2={'a','b','c'}
#set3=set1.union(set2)
set3= set1 | set2
print(set3)"""

"""set1={1,2,3}
set2={'blue','red','violet'}
set3={"john","jill"}
set4={"BMW","ferrrari"}

#my_set=set1.union(set2,set3,set4)
my_set= set1 | set2 | set3 | set4 
print(my_set)"""

# join set and tuple
"""set_1={"apple",1,2,4.5,"john"}
tuple_1=('red','pink')

a= set_1.union(tuple_1)
print(a)"""

#join sets
"""set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)"""

#intersection()  method will return a new set, that only contains the items that are present in both sets
"""set1={'john','jill','eva'}
set2={'jill', 'eva', 'harry'}

#set3=set1.intersection(set2)
set3= set1 & set2 # & method
print(set3)"""


#Keep the items that exist in both set1, and set2:
"""set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)"""

"""set1 = {"apple", 1, 0, "cherry"}
set2 = {False, "google", 1, "apple",2, True}

set3 = set1.intersection(set2)

print(set3)"""

#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#set3=set1.difference(set2)
#set3= set1 - set2        # using - operator
set3= set1.symmetric_difference(set2)
print(set3)