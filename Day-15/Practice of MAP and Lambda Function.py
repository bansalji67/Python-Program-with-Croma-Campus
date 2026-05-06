"""
Practice of MAP and Lambda Function
# Lambda Basics  

Q-1 Write a lambda function to add two numbers

add=lambda a,b :a+b
print(add(5,7))

Q-2 Write a lambda function to check if a number is even or odd.

check_even_odd= lambda x: "even" if x%2==0 else "odd"
num=int(input("Enter the Number:"))
print(f"{num} is {check_even_odd(num)}")

# Using map()
Q-3 Given a list of integers, use map() to create a new list with each number squared.

li=[x for x in range(1,11)]
squar_num=lambda x :x**2
res=list(map(squar_num,li))
print(res)

Q-4 Convert a list of strings to uppercase using map().

word=["hello","python","world"]
convert_upper=list(map(lambda x:x.upper(),word))
print(convert_upper)

# Using filter()  

Q-5 Given a list of numbers, filter out only even numbers.

li=[x for x in range(1,11)]
filter_even_only= lambda x:x%2==0
res=list(filter(filter_even_only,li))
print(res)

Q-6 Filter words that have length greater than 5 from a list of strings

word=["Hello","Students","How","are","you"]
check_length=lambda word : len(word)>5
res=list(filter(check_length,word))
print(res)

#Using reduce()

Q-7 Find the sum of all elements in a list using reduce()

from functools import reduce
li=[x for x in range(1,11)]
sum_all_elements=lambda x,y:x+y
print(reduce(sum_all_elements,li))

Q-8 Find the product of all numbers in a list.

from functools import reduce
numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,numbers)
print(product)

# Combination of lambda + map   

Q-9 Given a list of numbers, return a list where each number is multiplied by 10.

numbers=[1,2,3,4,5]
result=list(map(lambda x:x*10,numbers))
print(result)


Q-10 From a list of numbers, filter out all numbers divisible by 3

condition: Combination of lambda + filter

numbers=[1,3,4,6,7,9,10,15,12,20,24]
result=list(filter(lambda x :x%3==0,numbers))
print(result)

Q-11 Find the maximum number in a list using reduce()
condition:- Using reduce() for maximum

from functools import reduce
li=[12,34,5,68,56,32,66,89,3,7]
find_max=lambda x,y:x if x>y else y
res=reduce(find_max,li)
print(res)

Q-12 Given a list of names, use map() to return names with their first letter capitalized.

li=["ravi","mohan","naresh","suresh","kamal"]
first_letter_upper=list(map(lambda li:li.capitalize(),li))
print(first_letter_upper)

"""



