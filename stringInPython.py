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

#MODIFYING STRINGS
a = " Hello, World! "
print(a.upper()) #CAPITALIZES EVERYTHING LIKE THIS
print(a.lower()) #lowercases everything like this
print(a.strip()) #removes whitespace from beginning and the end
print(a.replace("H", "J")) #replaces H with J, creating a Jello World
print(a.split(","))

#CONCATENATION
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Formatting Strings

#REMEMBER YOU CANNOT PUT STRINGS AND NUMBERS TOGETHER LIKE THIS:
#age = 36
#txt = "My name is John, I am " + age
#print(txt) This will produce an error

#inserting numbers into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #prints with the number in the string

#format method() takes unlimited number of args and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #includes the numbers in tuple into the order
print(myorder.format(quantity, quantity, quantity)) #includes the same number
print(myorder.format(quantity, quantity)) #includes the name and predicts third numbers
#print(myorder.format(quantity)) ERROR

myorder = "I want to pay {2} dollars ofr {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #Prints numbers in desired order

#ESCAPING
#THIS IS AN ERROR OF DOUBLE QUOTES:
# txt = "We are the so-called "Vikings" from the north."
#To Fix use /
txt = "We are thee so-called \"Vikings\" from the North." #This is valid use of double quotes

#Other Examples:
#\' Single quote
#\\ Backslash
#\n New Line
#\r Carriage return
#\t Tab
#\b Backspace
#\f Form Feed
#\ooo
#\xhh

#STRING METHODS (Return New Values, Do not transform the original string:)
#Capitalize() : Converts the first character to uppercase
#casegold() : Converts string into lowercase
#center() : Returns a centered string
#count() : Returns the number of times a specified values occurs in a stirng
#encode() : Returns an encoded version of the string
#endswit() : Returns true if the string ends with the specified value
#expandtabs() : Sets the tab size of the string
#find() : Searches the string for a specified value and return sthe position of where it was found
#format() : Formats specified values in a string
#format_map() : Formats specified values in a string
#index() : Searches the string for a specific value and returns the position of where it was found
#isalnum() : Returns True if the characters in the string are alphanumeric
#isalpha() : Returns True if all characters in the string are in the alphabet
#isdecimal() : Returns True if all characters in the string are decimals
#isdigit() : Returns true if all characters in the string a are digits
#isidentifier() : Returns True if the string is an identifier
#islower() : Return True if all characters in the string are lower case
#isnumeric() : Returns True if all characters in the string are numeric
#isprintable() : Returns True if alL characters in the string are printable
#isspace() : Returns True if all characters in the string are whitespaces
#istitle() : Returns True if the string follows the rule of a title
#isupper() : Returns True if all characters in the string are upper ase
#join() : Joins the elements of an iterable to the end of the string
#ljust() : Returns a left justified version of the string
#lower() : Converts a string into lowercase
#lstrip() : Returns a left trim version of the string
#maketrans() : Returns a translation table to be used in translations
#partition() : Returns a tuple where the string is parted into three parts
#replace() : Returns a string where a specified value is replaced with a specified value
#rfind() : Searches the string for a specified value and returns the last position of where it was found
#rindex() : Searches the string for a specified value and returns the last position of where it was found
#rjust() : Returns a right justified version of the stsring
#rpartition() : Returns a tuple where the string is parted into three parts
#rsplit() : Splits the string at the specified separator, and returns a list
#rstrip() : Returns a right trim version of the string
#splitlines() : Splits the string at the line breaks and returns a list
#startswith() : Returns a true if the statement starts with the specified value
#strip() : Returns a trimmed version of the string
#swapcase() : Swap cases, lower case becomes upper case and vice versa
#title() : Converts teh first character of each word to upper case.
#translate() : Returns a translated string
#upper() : Converts a string into upper case
#zfill() : Fills the string with a specified number of 0 values at the beginning










