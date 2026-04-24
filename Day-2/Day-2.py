a=27
b=34
c=a+b
print(c)

"""
IDLE:- Integrated Development Learning Enviornment

Python's Built -in Functions

print

print("Hello World!")

a=100

print('a')
print(a)
print('Aman')
print('''Aman''')

a=34
print('Hello,a')
print('Hello',a)
print('hello','a')

Input :- (it is used to ask value from the user)

----------
its doing concatination coz inputbox always consider value as a text or string

a=input("Enter A Number:")
b=input("Enter B Number:")    
c=a+b
print("Addition :",c)

Int:-- it is used to convert a value into integer(numerical value)

a=int(input("Enter A Number:"))
b=int(input("Enter B Number:"))   
c=a+b
print("Addition :",c)

Float:-- it is used to conver a value to numerical data also support to decimal value)

a=float(input("Enter A Number:"))
b=float(input("Enter B Number:"))   
c=a+b
print("Addition :",c)

Buit in Functions
print,input,float,int

"""

'''
# WAP to calculatethe Gross Salary of an employee where HRA is 20% and DA is 30% of his basic salary

  Hint:= Gross Salary=Basic Salary + HRA + DA
  
'''
B=int(input("Enter your Basic Salary: "))
HRA=B*20/100
DA=B*10/100
gs=B+HRA+DA
print("Gross Salary:",gs)
