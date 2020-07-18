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
Fruits = tuple(listFruits)
# this is a tuple
print(Fruits)
tuple1 = tuple(("a", "b", "c"))
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

