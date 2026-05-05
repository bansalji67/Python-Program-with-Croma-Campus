"""
UDF :-

df function_name(parameters):  # Prototype
     definition

function_name(arguments)       # calling

def greet():
    print("Good Morning")      #Static

greet()

def greet(val):
    print("Good",val)  #Dynamic

greet("Morning")
greet("Noon")
greet("After Noon")
greet("Evening")

Function:- Function is a block of statement, that perform a specific task
           and return a value

def add(a,b):
    return a+b

print(add(20,30))

# We can assign values in parameters from right sides

def add(a,b=0,c=0):
    return a+b+c

print(add(20,30))

def add(*a):   # create tuple for add values dynamically and get sum
    print(a)
    print(type(a))
    return sum(a)
print(add(10,20,30,50))

*args   : for Tuple
**kargs : for Dictionary

def add(**a):
    return a

print(add(name="Rahul Kumar", Dept="IT"))

# Recursion :-

A function calls itself


def add():
    add()
add()

factorial=>5 =>5*4*3*2*1=>120

Q- WAF to write factorial numbers

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
print("Factorial number is:",fact(5))

# WAP to check a number if prime or not

def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return "Not Prime"
    return "Prime"
        

print(checkprime(17))

Q- WAF to find all the prime numbers from 1 to 100

def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
        

for i in range(2,101):
    if checkprime(i):
        print(i)

"""


       




