# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# Lists are mutable which means we can change it.

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

# Access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5])
print(thislist1[-4:-1])

# Check if the item exists

if "apple" in thislist1:
  print("Yes, 'apple' is in the fruits list")

# Change item value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Insert Items - insert() will insert an item at any specified index

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items - append() will add the items at the end of the list

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List - extend() will add the items from one list to another list
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove specified items from the list - remove() will removes the specified item from the list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove specified index - pop() method will remove the item from the specified index
# If you do not specify the index it will just remove the last item from the list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del keyword removes the specified index but it can also delete the whole list completely
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)

# clear() method will empty the list items but the list should be still there

thislist = ["apple", "banana", "cherry"]

# Loop through a list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop through the index numbers
# The iterable created below is [0, 1, 2]

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using while loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Sort lists alpha numerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True

thislist = ["apple", "banana", "cherry"]
thislist.sort(reverse=True)
print(thislist)

# The reverse() method reverses the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy() method will copy the list to another list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# list() will also copy the list

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join two lists
# Using + operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Using append() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Using extend() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# List Methods
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()