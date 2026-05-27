
# Abstraction
"""
Abstraction:- Show functionality,hide complexity
-Abstract Class
  -can not be instantiated/can not create an object
  -can contains abstract method

from abc import ABC,abstractmethod
class services(ABC):
    @abstractmethod
    def prereq(self):
        pass
    def ser1(self):
        print("This is Service1")
    def ser2(self):
        print("This is Service2")
    def ser3(self):
        print("This is Service3")

class myclass(services):
    def prereq(self):
        print("Done")
    def myfun(self):
        print("I am my fun from myclass")

obj=myclass()
obj.myfun()
obj.ser1()

# Super------------------------------------

class Parent:
    x=100
    def show(self):
        print("I am show function from parent class")

class child(Parent):
    x=30
    def child_show(self):
        print("I am child show",super().x)
        super().show()

obj=child()
obj.child_show()
obj.show()

# Super with Constructor ------------------

class Parent:
    def __init__(self):
        print("I am parent Constructor")
    x=100
    def show(self):
        print("I am show function from parent class")

class child(Parent):
    def __init__(self):
        super().__init__()
        print("I am child Constructor")
    x=30

    def child_show(self):
        print("I am child show",super().x)
        

obj=child()
obj.child_show()
obj.show()

# Method Resolution Order--------------

class A:
    def abc(self):
        print("I am A")
class B(A):
     def abc(self):
        print("I am B")
class C(A,B):
     def abc(self):
        print("I am C")

print(C.mro())

##--------------------------------------------
class A:
    def abc(self):
        print("I am A")
class B(A):
     def abc(self):
        super().abc()
        print("I am B")
class C(B):
     def abc(self):
        super().abc()
        print("I am C")

print(C.mro())
obj=C()
obj.abc()

# Staticmethod

class myclass:
    x=100
    def myfun(self):
        print("Value of X is",self.x)
    
    @staticmethod
    def myfun2():
        print("Welcome to my page")
obj=myclass()
obj.myfun()
myclass.myfun2()     # Directly we can call the function using class
print(myclass.x)

"""








   