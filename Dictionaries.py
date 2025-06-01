# Dictionaries are used to store data values in key:value pairs.
# A Dictionary is a collection which is ordered, mutable which means changeable and do not allow duplicate values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))

# The values in dictionary items can be of any data type.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

# Accessing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# There is also get() method which will give you the same result.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

# The keys() method will return a list of all the keys in the dictionary.

print(thisdict.keys())

# Add a new item to the dictionary and verify if the keys list gets updated as well.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

car["color"] = "white"

print(x)

# The values() method will return a list of all the values in the dictionary.

print(car.values())

# Make a change in the value of the dictionary and see if the list of values also gets updated.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["year"] = 2020

print(x)

# The items() method will return each item in a dictionary, as tuples in a list.

print(thisdict.items())

# Check if the key exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict['year'] = 2020
print(thisdict)

# Update Dictionary - The update() method will update the dictionary with the items from the given argument.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# Adding Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist,
# the item will be added.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# Removing Items
# Using pop() method which will remove an item with the specified key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

# Using popitem() which will remove the last inserted value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name and it can also delete the dictionary completely.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# clear() method empties the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop through a dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
  print(x)
  print(thisdict[x])

# for x in thisdict.values():
#   print(x)
# for x in thisdict.keys():
#   print(x)

# Loop through both keys and values, by using the items() method

for x, y in thisdict.items():
  print(x, y)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and
# changes made in dict1 will automatically also be made in dict2.
# Make a copy of a dictionary with the copy() method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use dict() function

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# Access items in nested dictionaries

print(myfamily["child2"]["name"])

# Loop through nested dictionaries

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# Dictionary Methods
# clear()
# copy()
# fromkeys()
# get()
# item()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()