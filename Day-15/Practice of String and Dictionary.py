"""
String Programming Questions:-
# Basic

Q-1 Write a program to count the number of vowels in a string.

vowel="aeiouAEIOU"
count=0
str="Hello Students how are you"
for char in str:
    if char in vowel:
        count=count+1
print(count)

Q-2 Reverse a string without using built-in functions

str=["PYTHON"]
res=[]
for char in str:
    res=char[::-1]
    print(res)
    
Another way :-

txt="HELLO"
Reverse_txt=""
for char in txt:
    Reverse_txt=char+Reverse_txt
print(Reverse_txt)

Q-3 Check whether a string is a palindrome

txt="madam"
is_palindrom=True
i,j=0, len(txt)-1
while i<j:
    if txt[i]!=txt[j]:
        is_palindrom=False
        break
    i=i+1
    j=j-1
print(is_palindrom)

Another way :-

txt="madam"
print(txt==txt[::-1])

Q- 4 Count uppercase and lowercase letters in a string

str="Hello Students How Are You Doing Today"
count_upper=0
count_lower=0

for char in str:
    if char.isupper():
        count_upper=count_upper+1
    elif char.islower():
        count_lower=count_lower+1
        
print("Upper Case Count is:",count_upper)
print("Lower Case Count is:",count_lower)

Q-5 Replace all spaces in a string with _

txt="hello how are you"
result=txt.replace(" ","_")
print(result)

# Intermediate Level :-

Q-6 Find the frequency of each character in a string.

txt="Hello Students how are you"
freq={}

for char in txt:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1
print(freq)

Q-7 Remove duplicate characters from a string.

txt="Hello students how are you"
unique_list=[]

for char in txt:
    if char not in unique_list:
        unique_list.append(char)
result="".join(unique_list)
print(result)

Q-8 Find the first non-repeating character in a string.

txt="swiss"
freq={}
for char in txt:
    freq[char]=freq.get(char,0)+1 # Count Frequency

for char in txt:                # find first non repeating
    if freq[char]==1:
        print(char)
        break
        
# Find the all non-repeating character in a string

txt="swiss"
freq={}
for char in txt:
    freq[char]=freq.get(char,0)+1 # Count Frequency

result=[char for char in txt if freq[char]==1]
print(result)

Q-9 Check if two strings are anagrams.

s1="listen"
s2="silent"
print(sorted(s1)==sorted(s2))

Q-10 Convert "hello world" → "Hello World" (title case without using .title()).

txt="Hello World"
result=""
words=txt.split()

for word in words:
    result= word[0].upper() + word[1:]+" "
print(result.strip())

Q-11 Find the longest word in a sentence.

txt="hello students how is going your day"
words=txt.split()
longest_word=""

for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print(longest_word)

Q-12 Compress a string like "aaabbc" → "a3b2c1"

Q-13 Count words, characters, and digits in a string.

txt="Hello 23 students how are you"
count_char=0
word_count=len(txt.split())
count_digit=0

for char in txt:
    if char.isalpha():
        count_char=count_char+1
    elif char.isdigit:
        count_digit=count_digit+1
        
        
        
print("word character",count_char)
print("Count Digit",count_digit)
print("Word Counts",word_count)

Q-14 Rotate a string left by n positions

txt="abcdefgh"
n=2
result=txt[n:]+txt[:n]  # [n:] start from 2 and [:n] end till 2, result = "cdef" + "ab"
print(result)

Q-15 Find all substrings of a given string.

"""





        


        

