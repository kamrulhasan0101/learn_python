fruits = {"apple", "banana", "lemon", "orange", "mango"}
# checking type of fruits variable
print(type(fruits))
# checking item is in the set or not
print("banana" in fruits)
# printing whole set as a loop
for x in fruits:
    print(x)
# Adding new items into set
fruits.add("added")
print(fruits)
# adding multiple items into set by update function
fruits.update(["orange", "new fruits", "grapes"])
print(fruits)
fruits.discard("banana") # can use pop(delete last) or clear to empty set
print(fruits)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)