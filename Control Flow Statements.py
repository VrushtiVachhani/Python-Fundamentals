# if statement

a = 33
b = 200
if b > a:
  print("b is greater than a")

# elif statement

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# else statement

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Shorthand if statement

if a > b: print("a is greater than b")

# Shorthand if...else statement

a = 2
b = 330
print("A") if a > b else print("B")

# Ternary Operators or Conditional Expressions

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and keyword

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or keyword

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# not keyword

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement
# to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

# Python Match Statements
# The match statement is used to perform different actions based on different conditions.
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
      print("No condition")

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches.
# Combine values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case.

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

# While loop

i = 1
while i <= 5:
    print(i)
    i = i + 1

# The break statement

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i = i + 1

# The continue statement

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else statement

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping through a string

for x in "banana":
    print(x)

# The break statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() function

for x in range(6):
  print(x)

# else in for loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass statement

for x in [0, 1, 2]:
  pass