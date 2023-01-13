#tuplesInPython.py

#ORDERED AND UNCHANGEABLE, cannot remove or add any items, AND ALLOW DUPLICATE VALUES

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ONE ITEMS TUPLES MUST HAVE A CINNA
thistuple = ("apple",)
print(type(thistuple)) #prints tuple

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #prints string

#of data type CLASS TUPLE
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Printing second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#To change a tuple, you must turn it into a list
#TUPLES ARE UNCHANGEABLE

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#You can add tuples to other tuples to make them bigger
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#UNPACKING TUPLES INTO MULTIPLE VARIABLES

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#NOTE: The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #LIST of the rest of the values

#Python will assign values to TROPIC until one is list to match the variable amounts
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#JOINGING AND MULTYPING TUPLES

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #doubles the same tuple

print(mytuple)

#Methods
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
