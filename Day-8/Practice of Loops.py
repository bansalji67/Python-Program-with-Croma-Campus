"""
# Basic for Loop

Q-1 Use a for loop to print numbers from 1 to 10.

for i in range(1,10):
    print(i)

Q-2 Print all even numbers between 1 and 20.

for i in range(1,20,1):
    if i%2==0:
        print(i)

Q-3 Print the sum of numbers from 1 to 10 using a for loop.

sum=0
for i in range(1,10):
    sum=sum+i
    print(sum)

Q-4 Take a number from the user and print its multiplication table up to 10.

t=int(input("Enter the Number:"))

for i in range(1,10+1):
    r=t*i
    print(r)

Q-5 Take a string and count the total number of characters using a for loop.

str=input("Enter the word: ")
count=0
for char in str:
    count=count + 1
print("Total number of character is:",count)

# Break Related Questions

Q-6 Print numbers from 1 to 10.Stop the loop when the number becomes 5.

for i in range(1,10):
    if i==5:
        break
    print(i)
    
# Continue Related Questions

Q-9 Print numbers from 1 to 10.Skip number 5

for i in range(1,10+1):
    if i==5:
        continue
    print(i)

Q-10 Print numbers from 1 to 20.Skip all even number

for i in range(1,20):
    if i%2==0:
        print(i)

Q-11 Print each character of the string "PYTHON".Skip the letter "O".

string="PYTHON"
for char in string:
    if char=="O":
        continue
    print(char)

# pass related Questions

Q-12 Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1,6):
    pass
    print(i)

Q-13 Loop from 1 to 10.If number is 6, just use pass.

for i in range(1,10):
    if i==6:
        pass
    print(i)


"""






















        

    
   
    
        
    


   

    

    
    
