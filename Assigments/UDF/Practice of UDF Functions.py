"""
Q-1 Write a function to print "Hello World

def function_hello():
    print("Hello World")

for i in range(1,5):
    function_hello()
    
Q-2 Create a function that takes a number and returns its square

def square(n):
    return n * n
print(square(5))

Another way:-

square=lambda x:x**2
print(square(4))

Q-3 Write a function to check whether a number is even or odd

def check_oddeven(n):
    if n%2==0:
        return "Even"
    return "Odd"
print(check_oddeven(17))

Another way :-

for i in range(1,5):
    n=int(input("Enter the number:"))
    check_oddeven(n)
    print(n,"is",check_oddeven(n))
    
Q-4 Create a function that returns the sum of two numbers.

def sum(a,b):
    return a + b
a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
print(f"sum of value {a} & {b} is:",sum(a,b))

Q-5 Write a function to find the maximum of three numbers.

def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
c=int(input("Enter the value of C: "))

print(f"Maximum number is:",find_max(a,b,c))

Q-6 Create a function that takes a string and returns it in uppercase.

def uppercase(str):
    return str.upper()

str=input("Enter your name:")
print(str.upper())

Q-7 Write a function to calculate the factorial of a number.

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)
    
print("factorial number is:",factorial(5))

Q-8 Create a function that checks if a number is positive, negative, or zero

def check_number(n):
    if n<=0:
        return "Negative number"
    return "Positive"
n=int(input("Enter the number:"))
print(f" {n} is",check_number(n))

Another way:-

def check_number(n):
    if n<=0:
        return "Negative number"
    return "Positive"

for i in range(1,5):
    n=int(input("Enter the number:"))
    check_number(n)
    print(f" {n} is",check_number(n))
    
Q-9 Write a function to count the number of vowels in a string

def count_vowels(str):
    vowels="aeiouAEIOU"
    count=0

    for char in str:
        if char in vowels:
            count=count+1
    return count
print("Number of vowels is:",count_vowels("Hello India"))

Q-10 Create a function that returns the length of a list (without using len()).

li=[12,34,56,67,89,56]
def find_length(li):
    count=0

    for char in li:
        count=count+1
    return count
print("length of a list is:",find_length(li))

# Intermedtiate Level :- 

Q-11 Write a function to check whether a number is prime

def checkPrime(num):
    for i in range(2,num):
        if num%2==0:
            return "Not Prime"
        return "Prime"
    
num=int(input("Enter the number:"))

print(f"{num} is",checkPrime(num))

Q-12 Create a function that returns the reverse of a string

def reverse_string(str):
    return str[::-1]

print(reverse_string("hello"))

Q-13 Write a function to find the sum of all elements in a list.

li=[12,34,56,78,33,11]
def sum_function(li):
    return sum(li)

print(sum_function(li))

Q-14 Create a function that returns the second largest number in a list.

def second_largest(num):
    unique_number=list(set(num))  # remove duplicates
    unique_number.sort()
    return unique_number[-2]

print(f"second largest number is:",second_largest([10,84,56,76,12]))

Q-15 Write a function to remove duplicates from a list.

li=[12,45,67,12,64,45,78,98]

def remove_duplicate(li):
    unique_list=list(set(li))
    return unique_list
print(remove_duplicate(li))

Q-16 Create a function that checks if a string is a palindrome

def is_palindrome(txt):
    return txt==txt[::-1]

print(is_palindrome("madam"))

Another way:-

def is_palindrome(txt):
    txt=txt.replace(" ","").lower()
    return txt==txt[::-1]
print(is_palindrome("Spider man"))

Q-17 Write a function that takes a list and returns only even numbers

list1=[22,14,2,67,78,90,55,21,7,10]
unique_list=[]
def pick_even(list1):
    for num in list1:
        if num%2==0:
            unique_list.append(num)
    return unique_list
print(pick_even(list1))

Q-18 Create a function to count frequency of each element in a list.

list1=[34,12,46,34,78,3,7,12,7]
def count_freq(list1):
    freq={}
    for num in list1:
        if num in freq:
            freq[num]=freq[num]+1
        else:
            freq[num]=1
    return freq
print(count_freq(list1))

Q-19 Write a function that merges two lists into one.

list1=[1,4,5,12,10,8]
list2=[87,34,56,71]

def merge_list(list1,list2):
    return list1 + list2

print(merge_list(list1,list2))

Q-20  Create a function to calculate simple interest.

def Calculate_interest(P,I,T):
    return (P * I * T)/100

print("Total Inerest is:",Calculate_interest(740000,2,3))

Advance Level :-

Q-21 Write a function using recursion to find factorial.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print("factorial number is:",factorial(5))

Q-22 Create a recursive function for Fibonacci series.

def fibonacci(n):
    if n<=0:
        return "invalid output"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(1,7):
    print(fibonacci(i),end=" ")

Q-23  Write a function that accepts *args and returns their sum.

def add(*a):
    return sum(a)
print("Total of all elements is:",add(10,34,56,78))

Q-24 Write a function that accepts **kwargs and prints key-value pairs

def add(**a):
    return a
print(add(name="Hari",ID=3456))

Q-25 Create a function decorator that prints "Function Started" and "Function Ended".

def my_decorator(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()

Q-26 Write a function that returns another function (closure concept).

def outer(x):
    def inner(y):
        return x + y
    return inner
add_val=outer(5)
print("sum of two value is:",add_val(3))

Q-27 Create a function to sort a list without using built-in sort()

list1=[3,45,12,6,9,4,22,56,34]

def sort_list(list1):
    n=len(list1)

    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
print(sort_list(list1))

Q-28  Write a function that finds common elements in two lists

list1=[12,45,67,73,8,3,90,11]
list2=[66,45,8,55,89,90,11,3]


def common_elements(list1,list2):
    common_list=[]
    for num in list1:
        if num in list2:
            common_list.append(num)
    return common_list
print("common elements are:",common_elements(list1,list2))

Q-29 Create a function to flatten a nested list.

def flattern_list(nested_list):
    flat_list=[]

    for item in nested_list:
        if isinstance(item,list):
            flat_list.extend(flattern_list(item))
        else:
            flat_list.append(item)

    return flat_list
print(flattern_list([1,[2,[3,4],5],6]))

Q-30 Write a function that validates an email format.

def validate_email(email):
    if "@" in email and "." in email:
        if email.index("@")< email.rindex("."):
            return True
    return False

print(validate_email("xyz@gmail.com"))

Challenge Level :-

Q-31 Write a function to implement binary search.

def binary_search(arr,target):
    left=0

    right=len(arr)-1

    while left <=right:
        mid=(left + right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right= mid - 1
    return -1
arr=[2,5,8,10,16,22,59]
print(binary_search(arr,22))

Q-32  Create a function to generate all substrings of a string

def get_substring(txt):
    substring=[]

    for i in range(len(txt)):
        for j in range(i+1,len(txt)+1):
            substring.append(txt[i:j])
    return substring

print(get_substring("common"))

Q-33 Write a function to check anagram strings

def is_anagram(str1,str2):    # function check same characters different orders
    return sorted(str1)==sorted(str2)

print(is_anagram("listen","silent"))
print(is_anagram("gopal","oglap"))

Q-34 Create a function to rotate a list by k positions

def rotate_list(list1,k):
    n = len(list1)
    k=k % n    # handle k > n
    return list1[-k:]+ list1[:-k]

print(rotate_list([1,2,3,4,5],2))

Q-35  Write a function to find the first non-repeating character

def first_non_repeating(txt):
    freq={}

    #counting frequency
    for char in txt:
        freq[char]=freq.get(char,0)+1  # to add characters's value in dictionary

        # find first not repeating

    for char in txt:
        if freq[char]==1:
            return char
    return None
print(first_non_repeating("aabbcdeed"))

Q-36 Create a function to compress a string (e.g., "aaabb" → "a3b2")

Q-37 Write a function to implement LRU logic (basic idea

"""


            
    


        
        


    
        
    

    



    

    




