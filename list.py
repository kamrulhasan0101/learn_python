fruitList = ["apple", "mango", "orange", "dragon"]
print(fruitList)
fruitList[1]= "banana"
print(fruitList)
print(len(fruitList))
if "banana" in fruitList:
    fruitList.remove("orange")
    print("yes, Banana was in the list and removed from list.")
print(fruitList)
fruitList.pop(0)
print(fruitList)
del fruitList[0]
print(fruitList)
fruitList.clear()
print(fruitList)
fruitList.append("passion")
print(fruitList)
fruitList.insert(0, "mango")
print(fruitList)
newFruits = fruitList.copy()
print(newFruits)
pinkyList = ["apple", "mango", "orange", "dragon"]
mergelist = fruitList+pinkyList
print(mergelist)

