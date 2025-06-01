# Abstraction
# methods which are just defined but without implementation or method body
# partial implementation of class, we use this when what to implement is clear but how to implement is not clear.

# Abstract Class

from abc import ABC, abstractmethod
class A(ABC):
    def __init__(self,a):
        self.a = a

    #Abstract method
    @abstractmethod
    def met(self):
        pass

    #non abstract
    def met1(self):
        print("Class A met1")

    @abstractmethod
    def met2(self):
        pass

class B(A):
    def met(self):
        print("Class B met")

class C(B):

    def met2(self):
        print("Class C met2", self.a)

#we cannot create object for abstract method or class
#obj = A()  #error
b = C(10)
b.met()
b.met1()
b.met2()