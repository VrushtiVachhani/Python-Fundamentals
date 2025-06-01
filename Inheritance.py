# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


# Create a Child Class

class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() function

# class Student(Person):
#     def __init__(self, fname, lname):
# add properties etc.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready
# to add functionality in the __init__() function.

# Use the super() function
# Python also has super() function in which the child class will inherit the properties of the parent class or object.

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# By using the super() function, you do not have to use the name of the parent element, it will automatically
# inherit the methods and properties from its parent.
# Add properties

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Mike", "Olsen", 2019)


# Add Methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

