#booleansInPython.py

#Example of Boolean expressions
print(10 > 9) #Produces true
print(10 == 9) #Produces false
print(10 < 9) #produces false

#printing a message based on a conditional
a = 200
b = 33

if b > a:
    print("b is greater than a") #skips
else:
    print("b is NOT greater than a") #prints

#Evaluate a string and a number

print(bool("Hello")) #printstrue
print(bool(15)) #prints true

#Evaluate two variables
x = "Hello"
y = 15

print(bool(x)) #prints true
print(bool(y)) #prints true

#All values are true, except empty values
#Examples of empty, false values

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0

myobj = myclass()

print(bool(myobj)) #Returns a false value as well


#Returns boolean with functions

def myFunction() :
    return True

print(myFunction())

if myFunction():
    print("yes") #prints yes
else:
    print("NO")

#Checking if the value is a certain data type
x = 200
print(isinstance(x, int)) #prints TRUE


