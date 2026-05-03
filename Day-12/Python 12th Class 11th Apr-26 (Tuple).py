"""
List- List is a collection of hetregenous elements
a = [34,56,78,90]

Tuple:- Tuple is a collection of hetregenous elements
t = (32,46,56,78)

Way to Create Tuple:

t=(34,56,78,35)
t=(43,'Aman',34.6,'a',3+4j,True)
print(t)
t=()
t=tuple()
t=tuple([23,45,65,78,89])
t=tuple((23,45,65,78,89))
print(t)
print(type(t))

Tuple Support index:-

backward Index -1,-2,-3..etc
forward index   0,1,2,3..
tuple_name[index]

t=(34,56,78,35)
print(t)
print(t[2])
print(t[-3])

Tuple can be sliced
tuple[start_index : stop_index : step_index)

t=(34,56,78,35,6,56,25,48)
print(t)
print(t[3:6])
print(t[-5:-2])
print(t[3:])
print(t[:4])

Tuple also support Replication

t=(34,56,78,35,6,69,25,48)
print(t)
print(t*3) # it will repeat the tuple element for 3 times

Tupe can be traversed/itterate

t=(34,56,78,35,6,69,25,48)

for x in t:
    print(x)

Built-in Functions :-
  sum, max, min, len

t=(34,56,78,35,6,69,25,48)

print("Total of all values in tuple:",sum(t))
print("Maximum value in tuple is:",max(t))
print("Minimum value in tuple is:",min(t))
print("length of tuple is:",len(t))
  
Tuple's Method :-
  count, index

t=(23,56,78,23,45,67,23,45,789,66)
print(t)
print(t.count(23))
print(t.index(789))
print(t.index(45,5)) # to get the position of value 45 which is 2nd time

Tuple is immuteable (you can not change anything in the tuple)
Tuple is faster the list due to its immuteability

SET :- Set is also a collection of hetregenous elements

Ways to create a set

s={3,56,78,57,46}
s={243,'Aman',345.44,True,2+8j}
s=set()
s=set([23,45,56,78])
s=set((23,45,56,78))
print(s)
print(type(s))

Set is a collection of unique hetregenous elements

s={1,2,3,4,5}
print(s)
s={1,2,3,4,5,2,3,4,5,4,4,5,6,6,1,2,3,3,4,8,8,9,0}
print(s)   # it will remove the duplicate elements

Set has no index (set do not support INDEX)
Set can not be sliced
Set can not be replicate
But Set can be traverse/itterate

s={23,67,90,34,51,67,34}
print(s)

for x in s:
    print(x)

Built in Method
   sum, max, min, len

s={23,5,78,9}
print(s)
print("Total of all value is:",sum(s))
print("Maximum value is:",max(s))
print("Minimum value is:",min(s))
print("lenght of set is:",len(s))

Set's Methods
   add, update, remove, pop , discard, clear

s={12,34,56,78,12,78}
print(s)
s.add(99)  # add any element in sets
print(s)
s2={11,22,33}
s.update(s2) # Update another sets all elements in existing sets
print(s)  
s.pop()      # remove any elements from the set
print(s)
s.remove(78)
print(s)     # for remove any specific value
s.discard(101) # it will not give any error if value not exist in set
print
s.clear()    # clear all elements from the sets
"""





