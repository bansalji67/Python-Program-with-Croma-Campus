"""
Dictionary :- Dictionary is a collection of items
item means a pair of key and values {Key:Value}

Dictionary has no index
Dictionary can not be sliced
Dictionary can hold duplicate value but can not hold duplicate key
Dictionary can not be replicate
but Dictionary can be traverse/itterate

d={1:345,2:586,5:728,'A':970}
print(d)
print(d[2])
print(type(d))

for k in d:
    print(d[k])
    
Dictionary's Methods Keys

d={1:345,2:586,5:728,'A':970}
print(d)

for k in d:
    print(k)            # print only keys

d={1:345,2:586,5:728,'A':970}
for k in d.values():    # print only values
    print(k)
    
for k in d:
    print(d[k])         # print only values


d={1:345,2:586,5:728,'A':970}
for k in d.items():     # print only items
    print(k)

d={1:345,2:586,5:728,'A':970}

for k,v in d.items():
    print(k,v)

Update Method:-

d={1:345,2:586,5:728,'A':970}
print(d)
d1={4:999,5:222,6:888}
d.update(d1)
print(d)

remove method:-

d={1:345,2:586,5:728,'A':970}
d.pop(2)
print(d)
d.popitem()
print(d)

Strings:- String is a collections of characters
and it behave like a tuple

s="amankumar"
s="aman1234@abc.com"
s=""
s=str(123)
print(s)

String work on index
   forward and backward both

s="amankumar"
print(s)
print(s[3])
print(s[-4])

String can be sliced :-

s="amankumar"
print(s[2:7])
print(s[-7:-2])

String can be Replicate :-

s="Ha"
print(s*3)

Sring Can be traverse/itterate :-

s="AmanKumar"
for x in s:
    print(x)

Built-in functions:-
  sum, max , min , len

s="AmanKumar"
print(s)
print(max(s))
print(min(s))
print(len(s))

String's Method :- 
  upper , lower, Capitalization, strip, join

st="Aman Kumar"
print(st)
print(st.lower())
print(st.upper())
print(st.capitalize())
st="      Aman Kumar   "
print(st.strip()) # remove leading and trailing whitespace

st="aman is a good boy"
print(st.split())

st="PYTHON"
print("$".join(st))

st=['aman', 'is', 'a', 'good', 'boy']
print(" ".join(st))

String is immuteable you can not change anything in the string

### TIC_TAC_TOE Programme

li=[1,2,3,4,5,6,7,8,9]
player='X'
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
flag=0
while True:
    print(   "\n\t\t TIC TAC TOE")
    print(f"\n\t\t {li[0]}   | {li[1]} |  {li[2]} ")
    print("\t\t---------------")
    print(f"\t\t  {li[3]}  | {li[4]} | {li[5]} ")
    print("\t\t---------------")
    print(f"\t\t  {li[6]}  | {li[7]} | {li[8]} ")
    if flag==1:
        break
    print(f"n\n\t  Player {player} Turns : ",end="")
    ch=int(input())
    if ch in li:
        
        li[ch-1]=player
        for a,b,c in wins:
            if li[a]==li[b] and li[b]==li[c]:
                print(f"\n\t\tPlayer {player} WIN!")
                flag=1
                
        if player=='X':
            player='O'
        else:
            player='X'
    else:
        print("\n\t\t Already Selected Value! \n\t\t Try Again!")
"""
       
        

        
    
    


