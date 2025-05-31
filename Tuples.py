# Tuples are used to store multiple values in a single variable
# Tuple is a collection which is ordered and immutable which means that we cannot change it after creating.
# It also allows duplicate values

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

# Do not forget the comma when you are creating a tuple with one value only

thistuple = ("apple",)
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")  # it can contain values with multiple different data types
print(tuple1)

# Access Tuples

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])

# Check if the item exists or not

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Change tuple values
# Since tuples cannot be changed, so we first have to convert it into lists then change it and convert back to the tuples.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add items (convert to list first)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add one tuple to another, in this way also you can append or add any value at the end of any tuple without creating it into list.

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# remove() will remove itms but first we have to convert it into the list

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# You can delete the tuple completely
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

# Unpacking a tuple
# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the
# remaining values as a list.

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be
# assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the
# number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop through a tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop through the index numbers

thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
    print(thistuple[x])

# Using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join the tuples
# Using + operator

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Methods
# count()
# index()