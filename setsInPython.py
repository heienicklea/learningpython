#setsInPython.py

#a set is UNORDERED, UNCHANGEABLE (however, can add and remove) , and UNINDEXED
#DUPLICATES NOT ALLOWED

myset = {"apple", "banana", "cherry"}
print(myset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #ignores second apple

print(len(thisset)) #only prints 3, ignores fourth value


#OF CLASS SET
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Can use constructor to avoid curly braces
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#looping through sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

#Checking if banana is in the set
print("banana" in thisset) #Prints TRUE

#adding orange to the set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add from another set with Update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add from anything iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#WAYS TO REMOVE STUFF
#Remove feature will raise an error if the item does not exist
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Discard feature will not raise an eroor if the item does not exist
thisset = {"apple", "cherry"}

thisset.discard("banana")

print(thisset)


#JOINING AND KEEPING ONLY DUPLICATES
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#New list with duplicate items
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Keep all but not duplicate items
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#
#Methods
# add()	Adds an element to the set
#   clear()	Removes all the elements from the set
#    copy()	Returns a copy of the set
#   difference()	Returns a set containing the difference between two or more sets
#   difference_update()	Removes the items in this set that are also included in another, specified set
#   discard()	Remove the specified item
#   intersection()	Returns a set, that is the intersection of two other sets
#   intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#   isdisjoint()	Returns whether two sets have a intersection or not
#   issubset()	Returns whether another set contains this set or not
#   issuperset()	Returns whether this set contains another set or not
#   pop()	Removes an element from the set
#   remove()	Removes the specified element
#   symmetric_difference()	Returns a set with the symmetric differences of two sets
#   symmetric_difference_update()	inserts the symmetric differences from this set and another
#   union()	Return a set containing the union of sets
#   update()	Update the set with the union of this set and others
#
