"""
Pattern Building :

Q-1 Print below pattern

*****
*****
*****
*****
*****

print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

print("*****\n*****\n*****\n*****\n*****")

print("*****\n"*5)

for i in range(1,6):
    print("*"*5)

for i in range(1,6):
    print("*****")

for i in range(1,6):      # 1
    for j in range(1,6):  # 1,2,3,4,5
        print("*",end='')
    print()

Q-2 Print below Pattern

*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()

Q-3 Print below Pattern

1
12
123
1234
12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
    
Q-4 Print below pattern

1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

Q-5 Print below pattern

1
23
456
78910

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end='')
        k=k+1
    print()

Q-6 Print below pattern

A
AB
ABC
ABCD
ABCDE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()

Q-7 Print the below pattern

A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+64),end='')
    print()

A=65, B=66, C=67----Z=90
a=97, b=98, c=99----z=122

Q-8 Print the below pattern

A
BC
DEF
GHIJ
KLMNO

k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end='')
        k=k+1
    print()

Q-9 print the below pattern

*****
****
***
**
*

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()

Q-10 Print the below Pattern

    *
   **
  ***
 ****
*****

for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end='')
    for k in range(1,i+1):
        print("*",end='')
    print()

Q-11 Print the below pattern

    *
   ***
  *****
 *******
*********

for i in range(1,6):
    print(" " *(5-i)+"*" *(2 * i-1))   # " " * (5 - i) → prints spaces

                                       # "*" * (2*i - 1) → prints odd number of stars (1, 3, 5, 7, 9)
                                       

"""

    
    

    
        
        


