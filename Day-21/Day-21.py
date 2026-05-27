"""
OOPs:- Object Oriented Programming
       Class , Object
       
Pillars of OOPs: Encapsulation, Polymorphim, Inheritance,Abstraction

Class:- class is a virtual entity
        class is a blueprint of an object
        class is the representation of encapsulation

Method :

class class_name:
     class's_properties



class is a virtual entity :-

Example:-

class myclass:
    x=10
print(x)
        
object_name = class_name()

# Class is a blueprint of an object

Example:-

class myclass:
    x=10
    def abc(a):
        print("Hello India")


obj=myclass()
print(obj.x)
obj.abc()

# All Objects are individual :-

Example:-

class myclass:
    x=10
    def abc(a):
        print("Hello India")


obj1=myclass()
obj2=myclass()
obj3=myclass()
obj2.x=100
print(obj2.x)

# self :- Self is a current class object.

class utility:
    x=100
    def myfun(self):
        print("value of X is",self.x)
        
obj=utility()
print(obj.x)
obj.myfun()

# Constructor:- Constructor is a property of a method where,
  this method call automatically when an object will be created
  and the constructor name is __init__()


class utility:
    x=100
    def myfun(self):
        print("Value of X is",self.x)
    def __init__(self):                # use double underscore here
        print("I am Constructor")
        
obj=utility()

OOP's Properties (4 Main Pillars)

Encapsulation
we bind all the data members and member functions in a
single unit, it is called encapsulation

class utility:
    x=100
    def myfun(self):
        print("Value of X is",self.x)

-Inheritance :- Its a property of class where, this class's
                object can access the property of another class but, first
                you need to inherit the class

# Single Level Inheritance

class A: # Parent Class
    def myfunA(self):
        print("I am a function from class A")
class B(A): # Child Class
    def myfunB(self):
        print("I am a function from class B")

obj=B()
obj.myfunA()

# MultiLevel Inheritance

class A: 
    def myfunA(self):
        print("I am a function from class A")
class B(A): 
    def myfunB(self):
        print("I am a function from class B")
class C(B): 
    def myfunC(self):
        print("I am a function from class C")

obj=C()
obj.myfunC()
obj.myfunB()
obj.myfunA()

# Multiple Inheritance

class A:                                     # here A can not use B or c's property
    def myfunA(self):
        print("I am a function from class A")
class B:                                      # here B can not use A or c's property
    def myfunB(self):
        print("I am a function from class B")
class C(A,B):                                 # but C Use both A&B Properties
    def myfunC(self):        
        print("I am a function from class C")

obj=C()
obj.myfunC()
obj.myfunB()

# Inherical Inheritance

class A:                                     
    def myfunA(self):
        print("I am a function from class A")
class B(A):                                      
    def myfunB(self):
        print("I am a function from class B")
class C(A):                                 
    def myfunC(self):        
        print("I am a function from class C")

obj=C()
obj.myfunC()
obj.myfunB()
obj.myfunA()

# Hybrid Inheritance

class A:                                     
    def myfunA(self):
        print("I am a function from class A")
class B(A):                                      
    def myfunB(self):
        print("I am a function from class B")
class C(A):                                 
    def myfunC(self):        
        print("I am a function from class C")
class D(B,C):                                 
    def myfunC(self):        
        print("I am a function from class C")

obj=C()
obj.myfunC()
obj.myfunB()
obj.myfunA()

# Polymorphism ( poly(many) + morphism(forms) )
# When an entity have more than one behaviour is called polymorphism

def add(a,b):
    return a+b

# Function Overloading

print(add(10,20))   #addition
print(add('Aman','Kumar')) # Concatenation
print(add([1,2,3],[4,5,6])) # Extented

# Function Overriding


# Child will use its own property if Parent has same property

class A():
    def myfun(self):
        print("Hello India")
class B(A):
    def myfun(self):
        print("Hello World")
obj=B()
obj.myfun()

"""


        


