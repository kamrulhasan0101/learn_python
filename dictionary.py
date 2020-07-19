personDict = {
  "name": "kamrul",
  "age": "28",
  "ph": 1964
}
personDict["sex"]="male"
print(personDict.get('address',"Address Not Found"))
print(personDict)
# printing keys
for x in personDict:
    print(x)
# printing values
for x in personDict:
    print(personDict[x])
# printing values
for x in personDict.values():
    print(x)
# printing both keys and values
for x in personDict.items():
    print(x)
if "address" in personDict:
    print("Address found")
else:
    print("Address not found")
newDict = personDict.copy()
print(newDict)
anotherDict = dict(personDict)
print(anotherDict)
child1 = {
   "name" : "Emil",
   "year" : 2004
 }
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
myfamily = {
  "child1" : child1,
  "child2" : child2
}
print(myfamily)
print(myfamily['child1']['name'])

# Python code to merge dict using update() method
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict2.update(dict1)
print(dict2)
# Python code to merge dict using **
print({**dict1, **dict2})