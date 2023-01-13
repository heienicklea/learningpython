
print("HelloWorld")

if 5 > 2:
    print("Five is greater than Two!")

x = 5

#Codeand Spartans put together

y = "This is Python! *in Spartacus voice*" #fantastic new movie idea

#print("I want to say hello world")
print("Comments will stop that from happening")

#I
#Can
#Talk
#On
#More
#Than
#One
#Line


#Print numbers and strings
x = 5
y = "John"
print(x)
print(y)


#explicit creation of variables

#I really want a string
x = str(3) #this is a string that is '3'
print(type(x))
#I really want an integer
y = int(3) #this is an integer that is 3
print(type(y))
#I really want a float
z = float(3) #this is a float that is 3.0
print(type(z))

#These are the same things
x = "John"
print(x)
x = 'John'
print(x)

#These are different variables (Capitalized X will not overwrite x)
x = "John"
print(x)
X = "Sally"
print(x)

#legal variables names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal variable names:
#  --  2myvar = "John"
#  --  my-var = "John"
#  --  my var = "John"

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#Assigning Three Variables at Once (number of values must match on both sides)
x, y, z = 'Orange', 'Banana', 'Cherry'
print(x)
print(y)
print(z)

#Orange is the best, so it will take everything. Assigning all to one

x = y = z = "Orange"

#Creating a collection of fruits, then unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#All about output

x = "Python is Alright"
print(x)

#using a comma to output strings separetely
x = "Python"
y = "is"
z = "Alright"
print(x, y, z)

#or separating the words with plus signs (Notice no spaces will results in string combined)
x = "Python"
y = "is"
z = "Alright"
print(x + y + z)

#or separating the words (Spaces added to make correct sentence)
x = "Python "
y = "is "
z = "Alright"
print(x + y + z)


#Doing some math in print statement (printing 15)
x = 5
y = 10
print(x + y)

#ERROR ALERT
#String and integer together combined makes an error:
#x = 5
#y = "John"
#print(x + y) ERROR

#GLOBAL VERSUS INSIDE VARIABLES (THINK C)
x = "awesome" #This is a global variable

def myfunc():
    print("Python is " + x) #using the global variable within the function

myfunc() #will print Python is awesome using global variable

#you can declare global variables within functions, but looks weird usually

def myfunc2():
    global x
    x = "fantastic"

myfunc2() #new global x will not be declared without running this function, and python will
#awesome from above instead of fantastic

print("Python is " + x)

#PYTHON DATA TYPES

#Text Type: str
x = "Hello World" #string
print(type(x))

#Numeric Types: int, float, complex
x = 20
print(type(x)) #integer
x = 20.1
print(type(x)) #float
x = 1j
print(type(x)) #complex

#Sequence Types: list, tuple, range
x = ["apple", "banana", "cherry"]
print(type(x)) # list of fruits
x = ("apple", "banana", "cherry")
print(type(x)) # tuple of fruits
x = range(6)
print(type(x)) # range of numbers (0,5)

#Mapping Type: dict
x = {"apple" : "John", "age" : 36}
print(type(x))

#Set Types: set, frozenset
x = {"apple", "banana", "cherry"}
print(type(x)) # set of fruits
x = frozenset({"apple", "banana", "cherry"})
print(type(x)) #frozen set of fruits

#Boolean Type: bool
x = True
print(type(x)) #boolean

#Binary Types: bytes, bytearray, memoryview
x = b"Hello"
print(type(x)) #bytes
x = bytearray(5)
print(type(x)) ##byte array
x = memoryview(bytes(5))
print(type(x)) #memoryview

#None Type: NoneType
x = None
print(type(x)) #NoneType











