"""
Programming Questions – LIST

Q-1 WAP to create a list of integers and print its elements

l=[24,56,67,78,26]
print(l)

for n in l:
    print(n)

Q-2 WAP to find the sum and average of all elements in a list

l=[24,56,67,78,26]
print("Total of all elements of list is:",sum(l))

print("Average of list:",sum(l)/len(l))

Q-3 WAP to find the largest and smallest element in a list.

l=[24,56,67,78,26]
print("Largest value is:",max(l))
print("Smallest value is:",min(l))

Q-4 WAP to count the number of elements in a list without using len().

l=[24,56,67,78,26]
count=0
for n in l:
    count=count+1
print("Number of elements:",count)

Q-5 WAP to reverse a list without using built-in functions

numbers=[24,56,67,78,26]

reverse_list=[]

for i in range(len(numbers)-1,-1,-1):
    reverse_list.append(numbers[i])
print("Reversed_List:",reverse_list)

Q-6 WAP to check if an element exists in a list.

numbers=[24,56,67,78,26]
num=78
for i in numbers:
    if i==num:
        print("num is exist in list:",i)
    else:
        print("num is not exist in list:",i)

Q-7 WAP to remove duplicate elements from a list.

numbers=[24,56,67,78,26,56,67]
unique_list=list(set(numbers))
print("List after removing duplicates:",unique_list)

numbers=[24,56,67,78,26,56,67]
unique_list=[]

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("list after removing duplicates:",unique_list)

Q-8 WAP to sort a list in ascending and descending order.

n=[56,12,4,67,8,45,22,1,90]
n.sort()
print("sort list in asending order:",n)
n.reverse()
print("sort list in desending order:",n)

Intermediate Level:-

Q-9 WAP to merge two lists and remove duplicates.

num1=[24,5,78,33,79,55]
num2=[55,3,23,57,78,5,21]

merge_list=num1+num2
unique_list=[]

for num in merge_list:
    if num not in unique_list:
        unique_list.append(num)
print("Merge list without duplicate:",unique_list)

Q-10 WAP to find common elements between two lists.

number1=[24,5,78,33,79,55]
number2=[55,3,23,57,78,5,21]


common_list=[]
for num1 in number1:
    for num2 in number2:
        if num1==num2:
            common_list.append(num1)
print("common numbers in bot list is:",common_list)

Q-11 WAP to split a list into even and odd numbers.

num1=[23,45,66,12,5,78,93,48]

for i in num1:
    if i%2==0:
        print("element is even:",i)
    else:
        print("element is odd:",i)
        
Q-12 WAP to rotate a list by n positions

numbers=[10,20,30,40,50]  # number of position to rotate
n=2
length=len(numbers)
n= n % length           # handle case where n> length

for i in range(n):
    first=numbers[0]
    for j in range(length-1):
        numbers[j]=numbers[j+1]
    numbers[length-1]=first
print("list after rotation:",numbers)

Q-13 WAP to find the second largest number in a list.

num1=[23,45,66,12,5,78,93,48]
unique_number=list(set(num1))
unique_number.sort()
print("Second Largest number is:",unique_number[-2])


Q-14 WAP to flatten a nested list.

Q-15 WAP to count frequency of each element in a list.

num1=[23,45,67,45,12,3,78,5,12,6,3,99]
freq={}

for num in num1:
    if num in freq:
        freq[num]=freq[num]+1
    else:
        freq[num]=1
print(freq)

Q-16 WAP to replace all negative numbers with zero in a list.

num1=[12,-4,67,-54,22,90,-3,8,-27,55]

for n in range(len(num1)):
    if num1[n]<0:
        num1[n]=0
print(num1)

Advance Level:-

Q-17 WAP to remove all occurrences of a given element from a list.

numbers=[12,45,66,33,5,4,12,53,78,12,51]
elements=12
new_list=[]

for num in numbers:
    if num!=elements:
        new_list.append(num)
print(new_list)

Q-18 WAP to check if a list is a palindrome.

numbers=[1,2,3,2,1]
if numbers==numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

Q-19 WAP to find missing numbers in a given list of consecutive integers.

numbers=[1,2,4,6,7,8,10,12,15]
missing=[]

for i in range(min(numbers),max(numbers)):
    if i not in numbers:
        missing.append(i)
print("Missing Numbers:",missing)

Q-20 WAP to perform element-wise addition of two lists.


list1=[1,2,3]
list2=[4,5,6]
result=[]

for i in range(len(list1)):
    result.append(list1[i]+list2[i])
print(result)

Q-21 WAP to find the longest increasing subsequence in a list.

numbers=[10,22,9,33,21,50,41,60]

def list_simple(arr):
    longest=[]

    for i in range(len(arr)):
        current=[arr[i]]

        for j in range(i+1,len(arr)):
            if arr[j]>current[-1]:   # if next number is bigger
                current.append(arr[j])
        if len(current)>len(longest):
            longest=current
        return longest
print(list_simple(numbers))

Q-22  WAP to group elements based on frequency.

numbers=[1,2,2,3,3,4,5,4,7,8]

def group_by_freq(arr):
    freq={}

    # step count frequency

    for num in arr:
        if num in freq:
            freq[num]=freq[num]+1
        else:
            freq[num]=1

    # Group by frequency

    result={}

    for key,value in freq.items():
        if value in result:
            result[value].append(key)
        else:
            result[value]=[key]
    return result
print(group_by_freq(numbers))

Q-23 WAP to create a tuple and print its elements.

t=(12,34,56,3,5,78,22)

for n in t:
    print(n)

Q-24 WAP to find the length of a tuple

t=(12,34,56,3,5,78,22)
print("length of tuple:",len(t))


Q-25 WAP to find the maximum and minimum element in a tuple.

t=(12,34,56,3,5,78,22)
print("Maximum Number in tuple is:",max(t))
print("Minimum Number in tuple is:",min(t))

Q-26 WAP to convert a tuple into a list

t=(12,34,56,3,5,78,22)
L=[]

for i in t:
    L.append(i)
print(L)

Q-27 WAP to check if an element exists in a tuple.

t=(12,34,56,3,5,78,22)

def check_elements(t,elements):
    if elements in t:
        return "elements exist"
    else:
        return "elements not exist"
print(check_elements(t,21))

Q-28 WAP to count occurrences of an element in a tuple.

numbers=(12,45,66,33,5,4,12,53,78,12,51)


def count_elements(numbers,elements):
    return numbers.count(elements)

for num in numbers:
    print(num,"->",count_elements(numbers,num))

Another way:- 

t=(12,45,66,33,5,4,12,53,78,12,51)

for i in set(t):
    print(i,"->",t.count(i))

WAP to calculate the sum of all even numbers square of a
"""




    







    

    




        
    
        




    
    
    


