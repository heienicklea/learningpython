a = """I am writing a huge paragrap
in multuple lines
you 
cant 
stop 
how
many 
lines
I 
use
"""

print(a)

a = '''This
Works too
!'''

print(a)

#this also outputs the strings in multiple lines

#strings are technically arrays - like C

a = "Hello World"
print(a[1]) #prints E - Arrays start at zero

#printing each letter of banana
for x in "banana":
    print(x)

#finding the length of a string
a = "Hello, World!" #space, commas, and more included
print(len(a)) #prints 13


#Checking to see if something exists, return boolean true or false
txt = "The best thing in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is in the sentence") #confirming that free is in the text

#checking to see if something does NOT exist, returns boolean true or false

if "expensive" not in txt:
    print("No, 'expensive' is not in the sentence") #confirming that expensive is NOT in the text

#SLICING STRINGS
b = "Hello, World"
print(b[2:5]) #prints LLO

print(b[:5]) #slicing from the start prints hello (o, 1, 2, 3, 4) Stops at 5

print(b[3:]) #slicing form the fourth character beyond

#Negative Indexes
print(b[-5:-2]) #does not start at zero




