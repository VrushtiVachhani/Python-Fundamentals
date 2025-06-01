# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class

class MyClass:
    x = 5

# Create an Object

p1 = MyClass()
print(p1.x)

# The __init__() function

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do
# when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 18)
print(p1.name)
print(p1.age)

# The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person:{self.name}, {self.age}"
p1 = Person("John", 36)
print(p1)

# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello, My name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any
# function in the class.

class Person:
    def __init__(mysillyobject, name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello, My name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties

p1.age = 40

# Delete Object Properties

# del p1.age
# print(p1.age)

# Delete Objects

# del p1
# print(p1)

# The pass statement

class Person:
    pass