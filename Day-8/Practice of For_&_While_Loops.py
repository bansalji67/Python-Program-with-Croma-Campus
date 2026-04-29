"""
# For Loop Questions

Q-1 WAP to print numbers from 1 to 100.

for i in range(1,101):
    print(i)

Q-2 WAP to print all even numbers between 1 and 50.

for i in range(1,51):
    if i%2==0:
        print(i)

Q-3 WAP to print the sum of first n natural numbers.

n=int(input("Enter the number:"))
total=0

for i in range(1,n+1):
    total=total+i
print("sum of first",n,"natural number is:",total)

Q-4 WAP to print the multiplication table of a given number.

t=int(input("Enter the number:"))

for i in range(1,10+1):
    s=t * i
    print(s)
    
Q-6 WAP to count the number of vowels in a string.

vowel="AIEOUaieou"
string=input("Enter the word:")
count=0

for char in string:
    if char in vowel:
        count=count+1
print("Number of vowels:",count)

Q-8 WAP to print all prime numbers between 1 and 100.

count=0
n=100
for i in range(1,n+1):
    if n%i==0:
        count=count+1
        print(i)

Q-9 WAP to calculate the factorial of a number using a for loop.

n=int(input("Enter the number:"))
factorial=1

for i in range(1,n+1):
    factorial=factorial+i
print("Factorial of",n,"is:",factorial)

Q-10 WAP to print the reverse of a string using a for loop.

string=input("Enter the string :")
reverse=""

for char in string:
    reverse=char + reverse
print("Reverse String:",reverse)

# While Loop Related Questions:-

Q-11 WAP to print numbers from 1 to 50 using a while loop.

i=1

while i<=50:
    print(i)
    i=i+1

Q-12 WAP to print all odd numbers between 1 and 50.

i=1
while i<=50:
    if i%2 !=0:
        print(i)
    i=i+1

Q-13 WAP to calculate the sum of digits of a number.

num=int(input("Enter the number:"))
sum=0

while num !=0:
    digit=num %10
    sum=sum+digit
    num//=10
print("sum of digit:",sum)

Q-14 WAP to reverse a number using a while loop.

num1=int(input("Enter the number:"))
reverse=0

while num1 !=0:
    digit=num1 %10
    reverse=reverse *10+digit
    num1//=10
print("Reverse number:",reverse)

Q-15 WAP to find the factorial of a number using a while loop.

num=int(input("Enter a number: "))

factorial=1
i=1
if num<0:
    print("Factorial does not exist for negative numbers")
else:
    while i<=num:
        factorial=factorial * i
        i=i+1
    print("Factorial of",num,"is",factorial)

Q-16 WAP to keep taking input from the user until the user enters 0.

num1=int(input("Enter the number: "))

while num1!=0:  # use != sign for not equal to
    print("you entered:",num1)
    num1=int(input("Enter the number: "))
print("loop ended because you entered 0")

Q-17 WAP to find the largest digit in a number

num=int(input("Enter the number:"))
largest=0

while num>0:
    digit=num % 10
    if digit>largest:
        largest=digit
    num=num//10
print("Largest digit is:",largest)

Q-18 WAP to check whether a number is a palindrome.

num=int(input("Enter the number:"))
original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse * 10 + digit
    num=num//10
if original==reverse:
    print("Palindrom Number")
else:
    print("Not a Palindrom")

Q-19 WAP to print the Fibonacci series up to n terms.

a=0
b=1
n=int(input("Enter the number of terms:"))
m=1
while m<n:
    c=a+b
    print(c,end=' ')
    m=m+1
    a=b
    b=c

Q-20 WAP to implement a number guessing game using a while loop

import random

guess=random.randint(1,6)
num=0
while num!=guess:
    print("Wrong Guess!")
    num=int(input("Guess a number from (0 to 6):"))
else:
    print("You Guess Right Number:")

Q-21  WAP to print a number pattern using loops

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1

Q-22 WAP to count the frequency of each character in a string.

text=input("Enter the String:")
freq={}

for ch in text:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print("Character Frequencey:",freq)

text=input("Enter the strings:")
freq={}
i=0

while i<len(text):
    ch=text[i]
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
        i=i+1
print("Character Frequencey:",freq[ch])
for key,value in freq.items():
    print(key,":",value)

Q-23 WAP to print all Armstrong numbers between 1 and 1000.

for num in range(1,1000):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+(digit**3)
        temp=temp//10
    if sum==num:
        print(num)
        num=num+1

"""



            
    

    
        
    


        
    
    

    
        
        
        
            
        
    
