"""
Conditional Statement
if,if_else,Nested if_else,elif,complex condition

Looping:- for,While

IF
Syntax:-
if condition:
  True_Statement
else:
  False_Statement

if 10>5:
    print("Hello")

if 10>5:
    print("Hello") # here is condition is true so 1st print hello then
print("bye")         print bye its not the part of if condition here

if 10>50:
    print("hello")
else:
    print("bye")

Q_1 WAP to find greater value between two

a=10
b=20

if a>b:
    print("Greater Value:",a)
else:
    print("Greater Value:",b)
    
Q-2 WAP to check an entered number is Even/Odd

num=int(input("enter the number: "))

if num%2==0:
    print("Even Number:",num)
else:
    print("Odd Number:",num)

Nested IF_ELSE
Syntax:

if condition:
  if condition:
    True_Statement
 else:
    False_Statement
else:
    if condition:
       True_Statement
    else:
       False_Statement
a=100
b=100

if a>b:
    print("Greater Value:",a)
else:
    print("Greater Value:",b)
       
Q_3 WAP to find greater value b/w two also check for equal

a=100
b=100

if a>b:
    print("Greater Value:",a)
else:
    if a==b:
        print("Both are equal")
    else:
        print("Greater value:",b)

Q-4 WAP to check an entered number is positive, negative or zero

num=int(input("Enter the number: "))

if num>0:
    print("Number is Positive:",num)
else:
    if num<0:
        print("Number is Negative:",num)
    else:
        print("zero")

Q-5 WAP to check an entered character is vowel or Consonant

ch='W'

if ch=='A':
    print("vowel")
else:
    if ch=='E':
        print("vowel")
    else:
        if ch=='I':
            print("vowel")
        else:
            if ch=='O':
                print("vowel")
            else:
                if ch=='U':
                    print("vowel")
                else:
                    print("Consonant")
Use of Elif :

ch='W'

if ch=='A':
    print("vowel")
elif ch=='E':
      print("vowel")
elif ch=='I':
     print("vowel")
elif ch=='O':
     print("vowel")
elif ch=='U':
     print("vowel")
else:
     print("Consonant")
     
Complex Condition
write multiple conditions using logical operator

ch=input("Enter character")

if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
   print("vowel")
else:
   print("Consonant")

ch=input("Enter character: ")

Use of in :-

if ch in "AEIOUaeiou":  #in is Membership operator which is use to check existance of any character
   print("vowel")
else:
   print("Consonant")

"""



        


    
       
    









