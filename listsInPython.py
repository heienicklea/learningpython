#listInPython.py

mylist = ["apple", "banana", "cherry"] #store multiple items in one variable

print(mylist)

#List items are ordered, changeable, and allow duplicate values

#Determining list length

thislist = ["Apple", "Banana", "Cherry"]
print("The number of items are" + " " + str(len(thislist)))

#Lists can be any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Let lists have everything!
list1 = ["abc", 34, True, 40, "male"]

#NOTE: from python's perspective, lists are defined as objects with the data type 'list'

print(type(list1)) #prints <class 'list'>


#Instead of using brackets, you can use the list constructor
thislist = list(("Apple", "banana", "cherry")) #note double round brackets
print(thislist) #Prints ['Apple', 'Banana', 'cherry']

#Accessing list items
print(thislist[1]) # prints banana

#negative indexing
print(thislist[-2]) # prints banana

#Range of indexes
print(thislist[0:2]) #(0,1)

#Checking if item is present

if "Apple" in thislist:
    print("Yes, apples are in the list") #prints

#CHANGING ITEMS IN THE LIST
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #replaces banana with blackcurrant
print(thislist)

#Replaces two values with two values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "Watermelon"]
print(thislist)

#Replaces two values with one value, meaning there will only be apples and watermelons
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#inserting "Watermelon" as the third item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #inserts as the third item
print(thislist)

#inserting something to the end of the list
thislist.append("orange") #orange is added at the end
print(thislist)

#Appending another list to the current list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Note: the extend method does not have to append lists, you can add any iterable object (tuples,
#sets, and dictionaries etc.)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#removing specified items from the code
thislist.remove("orange") #only deletes first instance of orange
print(thislist)

#removing  a specified index
thislist.pop(1) #removes the second item
print(thislist)

#if you do not specify the index, ite removes the last item
thislist.pop() #deletes orange, the last item
print(thislist)

#Deleting the list
del thislist
#print(thislist) #Results in error

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #Prints empty brackets

#LOOPING THROUGH A LIST

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #prints each item on different  line

for i in range(len(thislist)): #caicuates length, then uses length to loop through range
  print(thislist[i]) #prints all three items

#While Loop through a list

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 #add one until reaches length of list
  print(i)
else:
    print("Hit end of list")

#Shortest syntax for printing a list, but does not make sense
[print(x) for x in thislist]


#LIST COMPREHENSION

#First, without list comprehension
#I want a list with only fruits that have A in it
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x) #adding fruits with a in it, to the NEWLIST

print(newlist) #prints apple, banana, mango

#Now, with list comprehension
#I want  alist with only fruits with E in it
newlist = [x for x in fruits if "e" in x]
print(newlist) #prints cherry and apple


#SORTING LISTS

#sorts alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sorts numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sorts descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#sorting based on how close it is to 50

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50 , 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#CASE Sensitive sorting
thislist = ["banana", "Orange", "kiwi", "Cherry"]
thislist.sort()
print(thislist)

#Avoid case sensitive sorting by specifying a key
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #sort alphabetically
print(thislist)

#COPY THE LISTS
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#OR

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#COMBINING LISTS TOGETHER

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) #prints ['a', 'b', 'c', 1, 2, 3]

#Appending with a for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x) #appends to end of list one by one

print(list1)

#Extend method to add all to the end of the list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#METHODS:
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list