# Types of Error :
"""
1. Syntax Error :- if there is an issue in your code, and is issue flaged by the interpreter/complier is called a syntax error.
                   The code will not run, and you need to fix this error.

a=10
print("india")
print("Hello"a)  # You need to fix this error

2. Runtime Error / Logical Error :- This Error can not be flagged by interpreter / Compiler, this error will occur at run time.
                                    Your programme will run in this case and you can fix or bypass the error
                                    This type of error is also called Exception
a=15
b=0
print("Division Start :")
print("Division :", a/b)  # Programme will Crash here 
print("Division End :")

3. Symmetric Error :- This Programme will not crash or stop but it will generate the wrong output sometimes, so in this case you
                      need to  find the bug and fix it

a=int(input("Enter the Value for A: "))
b=int(input("Enter the value for B: "))
print("Addition :",a*b)

# Exception Handling :- 
       
       try , except , finally , else

  If you have a doubt at a piece of code so you should write that code in TRY block

  You should except block with try and always use to write the alternate msg/code in the except block.

a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except:
      print("Found Error! ")   
print("Division End :")

#---------------You can Use Exception Class in your programme like below shwoing what type of error we are getting

a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except ZeroDivisionError as e:     # Shwoing type of Error
      print("Found Error! ",e)   
print("Division End :")

# Nested Except Case

a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except ZeroDivisionError as e:     # Shwoing type of Error
      print("Found Error! ",e)
except ValueError as e:
     print("Found Error! ",e)     
print("Division End :")

# Exception class is a mother class of every exception's classes

a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except Exception as e:
     print("Error!",e)     
print("Division End :")

# Use of Finally
# if my except can not handle the exception it will be crashed

a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except Exception as e:
     print("Error!",e)
finally:
     print("it will execute always")     
print("Division End :")

# Use of Else-----------------------------
  Else block will execute only when there is no error in try block

  
a=int(input("Enter the number of A: "))
b=int(input("Enter the number of B: "))
print("Division Start :")
try:
    print("Division :", a/b)
except Exception as e:
     print("Error!",e)
else:
     print("Division Done! ")
finally:
     print("it will execute always")     
print("Division End :")

try:- 
    Write your code, where you have doubt
except:-
    it will execute if there is an error
else:-
    it will execute if there is no error
finally:-
    it will execute always in every condition

# assert :- 
An assertion is a statement which is use to check the condition

assert condition , "Assert Message"
Assert is use to write a custom exception

age=int(input("Enter Age: "))
try:
    assert age>17 , "Age Should be 18+"
except AssertionError as e:
    print("Error!",e)
else:
    print("Welcome")

# RAISE
If you want to raise a custom error, so you can raise an error using raise keyword

age=int(input("Enter Age: "))
if age<18:
    raise ValueError("Age Should be 18+")
else:
    print("Welcome")

# Class 

class AgeError(Exception):
    pass
    
age=int(input("Enter Age: "))
if age<18:
    raise AgeError("Age Should be 18+")
else:
    print("Welcome")

class AgeError(Exception):
    pass
    
age=int(input("Enter Age: "))
try:
    if age<18:
        raise AgeError("Age Should be 18+")
    else:
        print("Welcome")
except AgeError as e:
    print("Error :",e)
print("Programme End!")
"""



