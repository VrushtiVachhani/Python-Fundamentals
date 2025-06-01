# Encapsulation
# Wrapping variables and code in class
# Variables cannot be accessed outside the class
# It ensures the controlled access using getters and setters

# Protected: Can be accessed in the derived class
# Private: Cannot be accessed directly in the derived class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        """Getter method to access private attributes"""
        return self.__age
    def set_age(self, new_age):
        """Setter method to modify private attributes"""
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive.")

# Creating an object of student class

student = Student("Vrushti", 22)

# Accessing public attribute
print(f"Student Name: {student.name}")

# Trying to access private attribute directly (will cause an error)
# print(Student.__age)  # This will raise an attribute error

# Accessing private attribute using getter
print(f"Student Age: {student.get_age()}")

# Modifying private attribute using setter
student.set_age(20)
print(f"Student Age: {student.get_age()}")

# Trying to set an invalid age
student.set_age(-5)  # This will not update the age

# Encapsulation: The __age attribute is private and cannot be accessed directly.
# Getter (get_age()): Allows controlled access to the private attribute.
# Setter (set_age()): Ensures the private attribute is modified with valid data.
# Security: Prevents direct modification of the age, ensuring valid values.