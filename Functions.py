# A Function is a block of code which only runs when it is called.
# You can pass data, known as parameters into a function.
# In python, a function is defined using def keyword.

def my_function():
  print("Hello from a function")
my_function()

# Arguments
# Information can be passed into functions as arguments
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want,
# just separate them with a comma.

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")   # 2 parameters and 2 arguments in this example

# Arbitrary Arguments
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the
# function definition.

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before
# the parameter name in the function definition.

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a list as an argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be
# treated as the same data type inside the function.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return values
# To let a function return a value, use the return statement

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement

def my_function():
    pass

# Positional-only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments.

def my_function(x, /):
  print(x)

my_function(3)

# Without , / you are actually allowed to use keyword arguments even if the function expects positional arguments

def my_function(x):
  print(x)

my_function(x = 3)
# But when adding the , / you will get an error if you try to send a keyword argument

# def my_function(x, /):
#   print(x)
#
# my_function(x = 3)

# Keyword Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments

def my_function(*, x):
  print(x)

my_function(x = 3)

# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments

def my_function(x):
  print(x)

my_function(3)

# But with the *, you will get an error if you try to send a positional argument

# def my_function(*, x):
#   print(x)
#
# my_function(3)

# Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

