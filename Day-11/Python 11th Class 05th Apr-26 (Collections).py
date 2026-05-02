"""
Pattern Building

Q-1 Print below pattern

A
AB
ABC
ABCD
ABCDE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()
    
Q-2 Print below pattern

*
**
***
****
*****

for i in range(1,6):
    print("*"*i)

Q-3 Print Below Pattern

     *
    **
   ***
  ****
 *****

for i in range(1,6):
    print(' '*(5-i),"*"*i)

Q-4 Print Below Pattern

1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)

Q-5 Print Below Pattern

1
12
123
1234
12345

st=""
for i in range(1,6):
    st=st+str(i)
    print(st)

Q-6 Print Below Pattern

0
909
89009
7890987
678908765
456789087654
34567890876543
2345678908765432
123456789087654321

st='0'
for i in range(10,0,-1):
    if i!=10:
      st=str(i)+st+str(i)
    print(st)

Collections:-

a = 10    # a is assign to 10
Variable , Constant


Sequence Data Type

 List,Tuple

List:- List is a collection of hetreogenous data type
li=[23,45,56,78,90]

Ways to create a list:-

li=[23,45,56,78,90]
li=[34,54.5,'A',True,'Aman',3+8j]
li=[]
li=list([23,45,67])
li=list((23,45,65,98))
print(li)
print(type(li))

List can work on INDEX
backward: -1,-2,-3,..
forward :  0,1,2,3,..

list_name[index_number]

li=[23,4,56,78,90]
print(li)
print(li[3])

# List also supports Slicing
list_name[start:stop:step]

li=[24,4,56,78,34,56,67,90]
print(li)
print(li[3:6:1])
print(li[2:5:1])
print(li[-5:-2])
print(li[-2:-5:-1])
print(li[-2:-7:-2])

List also Support Replication
List can traverse/itterate

li=[1,2,3,4]
print(li)
print(li*3)    # it will replecat the element of a list

li=[34,56,78,90]
for x in li:
    print(x+100)

li=[34,56,78,90]
for x in li:
    if x%2==1:
        print(x)


li=[12,34,56,67,89]
print(li)
print(li[1:4])
print(li[:3])  #start from 0
print(li[3:])  # end (length of the list)

List can work on Built-in Functions
   sum, max, min, len

li=[12,34,56,67,89]
print(li)
print(sum(li))
print(max(li))
print(min(li))
print(len(li))
print(sum(li)/print(len(li))

List's Methods
append, insert, extend

li=[23,45,67,89]
print(li)
li.append(99)
print(li)
li.insert(2,88)
print(li)
li2=[11,22,33,44]
li.extend(li2)
print(li)

Remove any element from the list :-

 pop, remove, clear

li=[23,45,67,89,54,5,67,78]
print(li)
li.pop()   # by default remove last element from the list
print()
li.pop(3)  # to remove specific element from the list
print(li)
li.remove(45) # when you don't know specific value's index number you can use it remove(value)
print(li)
li.clear()
print(li)    # to clear all the element from the list

use of Reverse, Sort :-

li=[23,78,63,56,67,67,54,34]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

Use of Index , Count in list

li=[23,78,63,56,67,67,54,34]
print(li)
print("count number of times repeat 67 value:",li.count(67))
print("give the position number of 56 value:",li.index(56))

"""






        
