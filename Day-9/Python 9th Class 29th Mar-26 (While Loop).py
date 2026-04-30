"""
For loop:-
syntax:-
for variable_name in range(start,stop,step):
     Statement
break,continue,pass,else

for i in range(1,10,1):
    print(i)
else:
    print(0)

for i in range(1,10,1):
    if i==4:
        break
    print(i)
else:
    print(0)

Continue :-

for i in range(1,10,1):
    if i==4:
        continue
    print(i)
else:
    print(0)

Nested for Loop :-

# WAP to check a number is Prime ?

num = int(input("Enter the Number:"))
count= 0

for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(num,"is prime Number")
else:
    print(num,"is not prime Number")

Nested for Loop: loop inside a loop

# WAP to find all the prime number from 1 to 50

for num in range(1,51):       # this loop run from 1 to 50
    count=0

    for i in range(1,num+1):  # This loop will check number is prime or not
        if num%i==0:
            count=count+1
    if count==2:
        print(num)

val=0
for num in range(1,100):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num)
        val=val+1
print("Total Prime Number :",val)

While Loop :-
Syntax:

Intialization
While Condition:
   Statement
   incr/decr
   
Used for Custom Condition
Example:-

a=1                       # Intialization
while a<=5:               # Condition
    print("Hello")        # statement
    a = a+1

a=1
while a<=3:
    sid=input("Enter student ID:")
    sname=input("Enter student Name:")
    a=a+1

ch='y'
while ch in "yY":
    sid=input("Enter Student ID:")
    sname=input("Enter Student Name: ")
    ch=input("Do you want to Continue(Y/N):")
break, continue, pass, else


a=1
while a<=5:
    print(a)
    if a==3:
        break
    a=a+1

a=1
while a<=5:
    print(a)
    if a==3:
        continue
    a=a+1

a=1
while a<=5:
    print(a)
    if a==3:
        continue
    a=a+1
    print(a)
"""

    

    

    










