"""my_list=[3,4,98,-56,7,-7,5,6]
#my_list.sort()
#my_list.sort(reverse = True)
my_list.reverse()
print(max(my_list))
print(min(my_list))
print(my_list)"""


"""numbers=[45,-7,9,76,3,3,8,49]
#numbers.append(90)
#numbers.insert(2,21)
#numbers.extend([35,45,55,65,75])
#numbers[3]=10
#numbers[1:4]=[91,92,93]
#numbers.remove(-7)
#print(numbers.pop(3))
#print(numbers)
print(numbers.count(3))"""


"""my_list=["jemie", 5.6, 45,False, 'tim ']
print("len of list is   ",len(my_list))          """

#use of  loops
"""my_list=['apple','cherry','lemon']
for i in my_list:
    print(i)"""


"""my_list=['apple','cherry','lemon']
i=0
while i<len(my_list):
    print(i)
    i=i+1                              """


"""my_list=['apple','cherry','lemon','guava']
new_list=[]
for i in my_list:
    if 'a' in i:
        new_list.append(i)

print(new_list)"""

"""my_list=['apple','cherry','lemon','guava']
new_list=[]
for i in my_list:
    if i !="apple":
        new_list.append(i)
print(new_list)   """

#convert into uppercase
"""my_list=['apple','cherry','lemon','guava']
new_list=[]
for i in my_list:
    x=i.upper()
    new_list.append(x)
print(new_list)    """

#access item
"""my_list=['apple','cherry','lemon']
print(my_list[2])
print(my_list[-2])"""

#check apple is present

"""my_list=['apple','cherry','lemon']

if "apple" in my_list:
    print("apple is present in list")"""

#copy list
"""my_list=['apple','cherry','lemon']
#list1 = my_list.copy()
list1 = list(my_list)
print(list1)    """

#join lists
list1 = [1,2,3,'car','True']
list2 = ['sam',4.5,7]
"""list3 = list1 + list2
print(list3)"""

for i in list2: #using for loop
    list1.append(i)

print(list1)
