"""
Controle Statement

if, if_else,Nested if_else,elif,complex condition
Looping:- we use loop to perform a same task again n again

for,while

for
syntax:-

for variable_name in range(start,stop,step):
   statement

for a in range(1,20,2):
    print("Hello")

print(* range(1,20,2))

print(* range(1,10,1)) # range accept only int datatype value

for i in range(1,10,1):
    print(i)

for i in range(1,10,1):
    print(i,end='\n') #its by default for new line

for i in range(1,10,1):
    print(i,end=' ') # print numbers in one line horizentally

for i in range(1,10,1):
    print(i,end='\t') # print numbers in one line horizentally with tab

for i in range(1,10): # by Default step=1
    print(i)

for i in range(5): # by default start from 0 and step will be 1 and run till 4 times
    print(i)

# WAP to print counting from 1 to 10

for i in range(1,11):
    print(i)
    
# WAP to print counting from 10 to 1

for i in range(10,0,-1):
    print(i)

# WAP to print counting from 1 to N

N=int(input("Enter range from 1 to N:"))

for i in range(1,N+1):
    print(i)
    
# WAP to find all the factors of a number
Hint:- 12=>1,2,3,4,5,6,12

n=int(input("Enter the Number:"))

for i in range(1,n+1):
    if n%i==0:
        print(i)

# WAP to count the factor a number
Hint:-12=>1,2,3,4,6,12=> 6 factors

count=0
n=int(input("Enter the Number:"))

for i in range(1,n+1):
    if n%i==0:
        print(i)
        count=count+1
print("Total Factors:",count)

# WAP to check an entered number is Prime

count=0
n=int(input("Enter the Number:"))

for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")

# Keywords:- Break,Continue,pass

# Break:- break exit from the current loop
for i in range(1,11):
    if i==4:
        break
    print(i)

# Continue:- Continue take the cursor to the next itteration
# or to the loop again, or it will skip the upcoming code
for i in range(1,11,2):
    if i==4:
       continue
    print(i)

# pass:- pass do nothing / pass the cursor to the next line
for i in range(1,11,2):
    if i==4:
       pass
    print(i)

"""

      
    



    







