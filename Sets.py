# Sets are used to store multiple values inside a single variable.
# A set is a collection which is unordered, immutable which means unchangeable and unindexed.
# Sets are unchangeable or immutable but you can add or remove an item from it.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets does not allow duplicate values.
# The value True and 1 are considered as same value in sets and are treated as duplicates.

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

# Access set items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Check if a particular item is present or not in the set

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Once a set is created, you cannot change an item but you can add one.
# Add items - add() method will add an item into the set

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add one set into another set using update() method

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Items
# Using remove() method - If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Using discard() method -  If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# We can also use pop() method - it will return the removed value and it will remove any random value

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear() method will empty the set

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will completely delete the set.

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# Loop through the set items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join sets
# The union() method will return a new set with all items from both sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# The join() method will allow you to join a set with other data types like lists, tuples, etc.

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
# The update() method will insert all items from one set to another.
# The update() changes the original set and does not return new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate values.
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#  The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of
# returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# The difference() method will return a new set that will contain only the items from the first set that are not
# present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will
# change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference_update(set2)
print(set3)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set
# instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference_update(set2)
print(set3)

# Set Methods
# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection()
# intersection_update()
# isdisjoint()
# issubset()
# issuperset()
# pop()
# remove()
# symmetric_difference()
# symmetric_difference_update()
# union()
# update()