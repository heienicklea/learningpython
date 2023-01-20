#functionsInPython

#python function is defined using the def keyword

def my_function():
    print("Hello from a function")

my_function()

#ARGUMENTS

#information can be passed into functions as arguments


#Adds standard last name
def my_function(fname):
    print(fname + " Refsnee")

my_function("Emil")

my_function("Tobias")

my_function("Linus")

#functions expect the same number of arguments back
#If you try to a call the function 1 or 3 argument you will get an error

def my_function2(fname, lname):
    print(fname + " " + lname)

#my_function2("Emil") This will be error
my_function2("Emil", "Refsnee") #this is right and prints Emil Refsnee


#arbitary arguments allow you pass tuples to a function without knowing how many arguments will  be passed

#Do not have how many will be produced for an individual argument

def my_function3(*kids):
    print("The youngest child is " + kids[1])


my_function3("Emil", "Tobias", "Linus")


#keyword arguments

def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Do not know keyword arguments will be passed
#Passes a dictionary that is named kid for the function
def my_function5(**kid):
    print(kid)
    print("His last name is " + kid["lname"])

my_function5( fname = "Tobias", lname = "Refsnee")



#Default values are used when the function is called without argument

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #prints norway as country
my_function("Brazil")


def my_function(food):
    print(food)
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]


#RETURN VALUE

def my_function(x):
    return 5 * x

print(my_function(3))

my_function(fruits)


#PASS STATEMENT when no content is needed for the function (does nothing(
def myfunction():
  pass

myfunction() #no error

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result



print("\n\nRecursion Example Results")
tri_recursion(1)
# 0 + 1
print("______")

tri_recursion(2)
# 0 + 1
# 0 + 1 + 2

print("______")

tri_recursion(3)
# 0 + 1
# 0 + 1 + 2
# 0 + 1 + 2 + 3

print("______")

tri_recursion(4)
# 0 + 1
# 0 + 1 + 2
# 0 + 1 + 2 + 3
# 0 + 1 + 2 + 3 + 4