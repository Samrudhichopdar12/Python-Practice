"""colors=["pink","orange","violet","grey"]
for i in colors:
    print(i)"""

#Looping Through a String
"""for i in "orange":
    print(i)    """


#use of break statement   
"""colors=["pink","orange","violet","grey","black","blue"]
for i in colors:
    print(i)

    if i =="grey" :
        break"""

#use of continue statement

"""colors=["pink","orange","violet","grey"]
for i in colors:
    if i == "orange" :
        continue
    print(i)"""
        

#range() Function

"""for i in range(1,11):
    print(i)"""

"""for i in range(3,36,6):
    print(i)   """

"""for i in range(7):
    if i == 5: break
    print(i)
else :
    print("finished") """

# Nested Loops   
adj=['tasty','big','sweet']
fruits=['apple','watermelon','mango']

for x in adj:
    for y in fruits:
        print(x,y)

        
      