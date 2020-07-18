fruits = ("apple", "banana", "lemon", "orange", "mango")
print(fruits[1:3])
for x in fruits:
    print(x)
if "passion" in fruits:
    print("yes, included")
else:
    print("Not Found")
print(len(fruits))
# changing values of tuple
listFruits = list(fruits)
listFruits[0] = "changed"
# this is a list
print(listFruits)
print(type(listFruits))
fruits = tuple(listFruits)
# this is a tuple
print(fruits)
print(type(fruits))
print("changed" in fruits)
tuple1 = tuple(("a", "b", "c"))
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3) # generates a error because of deleting tuple3

