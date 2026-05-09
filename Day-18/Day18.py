"""
File Handling :- You can write/read file using python
Type of Files :- 
1) Text File
2) Binary File

Text File (.txt, .xlsx, .doc etc)
Syntax :- File Opening

File Handler = open("Filename.extnsion","mode")
mode:-         r(read), w(write) , a(append) , r+ (read/write) , w+ (read/write) , a+ (append/read)

# How to open a file and write data into a file

file = open('student.txt','w')
file.write("Inder Kumar")
file.close()

# Using Append Mode

file = open('student.txt','a')
file.write("Hari Singh\n")
file.close()

# Write Multiple data using Writeline

li=['Tarun Kumar\n','Ravi Jha\n','Kiran Bansal\n']
file = open('student.txt','a')
file.writelines(li)
file.close()

# How to read data from a file

file=open('student.txt','r')
data=file.read()
print(data)
file.close()

file=open('student.txt','r')
data=file.read(20)         # read only 20 characters
print(data)
file.close()

file=open('student.txt','r')
data=file.readline()         # read only 1 Line
print(data)
file.close()

# Read all data using loop

file=open('student.txt','r')
while True:
    data=file.readline()         # read all data using loop
    print(data)
    if len(data)==0:
        break
file.close()

# Read data using readlines

file=open('student.txt','r')
data=file.readlines()    # Return a list of statement (read all lines at once)
for line in data:
    print(line)
file.close()

file=open('student.txt','r')
print(file.tell())     # Print the current position of the cursor in the file
data=file.read(10)
print(data)
print(file.tell())
file.close()

file=open('student.txt','r')
print(file.tell())     
data=file.read(10)
file.seek(20)         # it will take cursor to the specific position
print(data)
print(file.tell())
file.close()

# BINARY FILES:- (.bin, .dat etc)
Syntax:-
file_handler= open ('file_name.extension','mode')
mode:- rb, wb, ab , rb+ , wb+ , ab+

to dump(write) or to load (read) data into a binary file we required a pickle library

import pickle

pickle.dump('datapoints',file_handler)      # to write data
pickle.load(file_handler)                   # to read data

# Open and write data in a binary file

import pickle

file=open('emp.bin','wb')
pickle.dump('Rahul Kumar',file)
file.close()

# Append Data

import pickle

file=open('emp.bin','ab')
pickle.dump('Simran Khurana',file)
file.close()

import pickle

file=open('emp.bin','rb')
data=pickle.load(file)   # Read only first object
print(data)
file.close()


"""
import pickle

file=open('emp.bin','rb')
try:
    while True:
        data=pickle.load(file)
        print(data)
except:
    print("File Read Successfully")
file.close()