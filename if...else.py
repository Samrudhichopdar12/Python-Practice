"""a=30
b=400
if b >a :
    print("\n b is greater then a")
else:
    print("a is greater than b ")   """
#if b>a: print("b is greater than a")     #short hand if

#using elif
"""a=int(input("enter a value = "))
b=int(input("enter b value = "))

if a > b :
    print("a is greater than b ")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a ")   """    


#short hand if...else
"""a=4
b=56
print("A") if a>b else print("B")"""

"""a=2
b=2
print("A") if a>b else print("=") if a==b else print("B")"""


# using and
"""a=23
b=13
c=200
if a>b and c>a:
    print("c is greater than a and b ")"""


# using or
"""a=23
b=13
c=200
if a>b or a>c:
    print("At least one of the condition is true ")  """


#using Not
"""a=12
b=400
if not a>b :
    print("a is not greater than b ")  """   


#using nested if...else 
"""c=56
if c>10:
    print("c is above 10 ")
    if c>50:
        print(" also c is above 50 ")
    else:
        print("but c is not above 50 ")  """   


#pass 
"""a=23
b=600
if b>a:
    pass    """      


#to check num is even or odd
a= int(input("enter any num = "))
if a%2==0:
    print("num is even ")
else:
    print("num is odd ")        



