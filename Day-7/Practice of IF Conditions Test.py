"""
Singal Conditions

Q-1 Write a Python program to check if a number is positive.

num=int(input("Enter the Number:"))

if num>0:
    print("Numer is positive",num)

Q-2 Print "Eligible to vote" if age is 18 or above.

age=int(input("Enter the age:"))

if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

Q-3 Check if a number is divisible by 7

num=int(input("Enter the Number:"))

if num%7==0:
    print("Number is Divisible by 7")
else:
    print("Number is not Divisible by 7")

Q-4 Print "Pass" if marks are greater than 40

marks=int(input("Enter the marks:"))

if marks>=40:
    print("pass")
else:
    print("Fail")

Q-5 Check if a number is greater than 100.

num=int(input("Enter the number: "))

if num>=100:
    print("Greater than 100",num)
else:
    print("Less then 100",num)

Q-6 Display a message if temperature exceeds 45°C.

temp=float(input("Enter the Temperature:"))

if temp>=45:
    print("Temperature is exceed 45°C:")
else:
    print("Temperature is Normal")
    
Q-7 Check if a string length is more than 8 characters.

str=input("Enter any word :")

if len(str)>8:
    print("Entered string length is more than 8 characters")
else:
    print("Entered string length is less than 8 characters")

Q-8 Print "Logged In" if password matches "admin123"

password=input("Enter the Password:")

if password=="admin123":
    print("Logged in")
else:
    print("password incorrect")

Q-9 Check if a number is a multiple of 10.

num=int(input("Enter the number:"))

if num%10==0:
    print("Number is multiple of 10:")
else:
    print("Number is not a multiple of 10:")

Q-10 Print a warning if balance is below minimum limit.

Balance=int(input("Enter the Amount:"))
min_limit=1000

if Balance<min_limit:
    print("balance is below minimum limit")
else:
    print("balance is higher than limit")

# IF_ELSE (Two Condition)

Q-11 Check whether a number is even or odd.

number=int(input("Enter the Number:"))

if number%2==0:
    print("Number is Even:")
else:
    print("Number is Odd:")
    
Q-12  Find the largest of two numbers

num1=int(input("Enter the 1st Number:"))
num2=int(input("Enter the 2nd Number:"))

if num1>num2:
    print(f"The largest number is:",num1)
else:
    print(f"The largest number is:",num2)
    
Q-13 Check whether a person is eligible for driving license.

age=int(input("Enter your Age:"))

if age>=18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

Q-14 Print "Pass" or "Fail" based on marks.

marks=int(input("Enter the Marks:"))

if marks>=33:
    print("Pass")
else:
    print("Fail")
    
Q-15 Check whether a number is positive or negative.

num1=int(input("Enter the Number:"))
if num1>0:
    print("Number is Positive")
else:
    print("Number is Negative")
    
Q-16 Check whether a character is a vowel or consonant.

ch=input("Enter the character: ")
vowel="AIEOUaiou"

if ch in vowel:
    print("The Character is vowel:")
else:
    print("The Character is not vowel:")

Q-17 Check if a year is leap or not.

year=int(input("Enter the Year:"))

if year%4==0:
    print("The Entered year is Leap Year:")
else:
    print("The Entered year is not Leap Year:")

Q-18 Print "Valid Password" or "Invalid Password"

password1=input("Enter the Password:")
pass1="user123"

if password1==pass1:
    print("Valid password")
else:
    print("Invalid Password")

Q-19 Determine whether salary is taxable or not.

salary=int(input("Enter your Salary:"))
taxable_threshold=50000

if salary>taxable_threshold:
    print("Salary is Taxable:",salary)
else:
    print("Salary is not Taxable:",salary)

Q-20  Check whether a number is greater than 50 or not.

num1=int(input("Enter the Number:"))

if num1>50:
    print("The entered number is greater than 50:")
else:
    print("The entered number is not greater than 50:")

# NESTED IF–ELSE :

Q-21 Find the largest of three numbers.


num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))

if num1>num2:
    if num1>num3:
        print(f"The largest number is:",num1)
    else:
        print(f"The largest number is:",num3)
else:
        if num2>num3:
            print(f"The largest number is:",num2)
        else:
            print(f"The largest number is:",num3)
            
Q-22  Check whether a number is positive, negative, or zero

number=int(input("Enter the number:"))

if number>=0:
    if number==0:
        print("The number is zero:")
    else:
        print("The number is positive:")
else:
    print("The number is Negative:")
    
Q-23 Assign grades:

marks>90 --'A'
marks>75-- 'B'
marks>60-- 'C'
marks<60-- 'FAIL'

marks = int(input("Enter the marks: "))

if marks>90:
    print("Grade-A")
else:
    if marks>75:
        print("Grade-B")
    else:
        if marks>60:
            print("Grade-C")
        else:
            print("Fail")
            
Q-24  Check whether a triangle is equilateral, isosceles, or scalene.

side1=float(input("Enter the lenght of side 1: "))
side2=float(input("Enter the lenght of side 2: "))
side3=float(input("Enter the lenght of side 3: "))

if side1==side2:
    if side1==side3:
        print("The traingle is equilaterial")
    else:
        print("The traingle is isosceles")
else:
    if side2==side3 or side2==side1:
        print("The traingle is isosceles")
    else:
        print("The traingle is Scalene")

Q-25 Check whether a character is uppercase, lowercase, digit, or special character.

char=input("Enter the Character :")

if char.isupper():
    print("The character is an uppercase letter")
else:
    if char.islower():
        print("The character is an lowercase letter")
    else:
        if char.isdigit():
            print("The character is digit")
        else:
            print("The character is special character")
            
Q-26 Calculate electricity bill using slab-wise rates

Condition:
WAP to calculate the electricity bill
  if 500 units used - Pay Rs 5 for each unit
  if 700 units used - Pay Rs 10 for each unit
  if 1000 units used - Pay Rs 15 for each unit
  if more than 1000 unit used - Pay 20 Rs each unit

u=int(input("Enter the units which you consumed:"))

if u<=500:
    print("your bill is Rs:",u*5)
else:
    if u>500 and u<=700:
        print("your bill is Rs:",u*10)
    else:
        if u>700 and u<=1000:
            print("your bill is Rs:",u*15)
        else:
            print("your bill is Rs:",u*20)
            
Q-27 Validate login using username and password

correct_username="admin"
correct_password="admin123"

username=input("Enter the Username: ")
password=input("Enter the Password: ")

if username==correct_username:
    if password==correct_password:
        print("Login successfully")
    else:
        print("incorrect password")
else:
    print("incorrect username")
  
Q-28 Check student result using marks of 3 subjects

sub1=int(input("Enter the marks of sub1:"))
sub2=int(input("Enter the marks of sub2:"))
sub3=int(input("Enter the marks of sub3:"))

total_marks=sub1+sub2+sub3
Average_marks=total_marks/3

if Average_marks>=50:
    if Average_marks>=75:
        print("The student has passed with distinction")
    else:
        print("The student has passed")
else:
    print("The student has faild")


"""



    

        



             
        

        
        



    




        

