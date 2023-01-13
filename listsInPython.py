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
