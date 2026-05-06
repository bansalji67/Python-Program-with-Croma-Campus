"""
Advance Python
   lambda, map, filter , reduce

def cube(num):
    return num **3
print(cube(7))

function_name = lambda parameter : definition
function_name(argument)

Use of lambda function:-

cube=lambda num:num**3
print(cube(7))

add=lambda a,b : a+b
print(add(34,67))

li=[x for x in range(1,11)] # List Comprehenssion
print(li)

li=[x**2 for x in range(1,11)] 
print(li)

Q-1 WAP to calculate cube all elements of a list

li=[x for x in range(1,11)]

cube = lambda num : num**3

for i in li:
    print(cube(i))

# MAP :- MAP work with collection and function

cube = lambda num : num**3
li=[x for x in range(1,11)]
print(li)

res= list(map(cube , li)) # here cube is function li is collection
print(res)

# anonymous function

li=[x for x in range(1,11)]
print(li)

res=list(map(lambda num : num **3,li))
print(res)

Another way :- 

res=list(map(lambda num : num **3,[x for x in range(1,11)]))
print(res)

# WAP to find all Even Numbers

# FILTER :-
# Filter can accept only those function/method who return only boolean answer

checkEven=lambda num : num%2==0
li=[x for x in range(1,11)]

res=list(filter(checkEven,li))
print(res)

# REDUCE  # before use it need to import it from functools

from functools import reduce

add=lambda a,b:a+b
li=[1,2,3,4,5,6,7,8,9,10]

print(reduce(add,li))

add=lambda a,b:a+b
li=[1,2,3,4,5,6,7,8,9,10]

print(reduce(add,li))

# WAP to calculate the sum of all even number's square of a list

from functools import reduce
li=[x for x in range(1,11)]
even=list(filter(lambda x:x%2==0,li))
even_sq=map(lambda x:x**2,even)
even_sq_sum=reduce(lambda a,b:a+b,even_sq)
print(even_sq_sum)

Another WAY:-

from functools import reduce
li=[x for x in range(1,11)]
even_sq_sum=reduce(lambda a,b:a+b,map(lambda x:x**2,filter(lambda x:x%2==0,li)))
print(even_sq_sum)

"""





