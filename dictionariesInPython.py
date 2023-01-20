#dictionariesInPython.py

#dictionary items are ordered, changeable, but DOES NOT ALLOW DUPLICATES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #Prints {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(thisdict["brand"]) #prints Ford

#Can even include boolean values
thisdict = {
  "brand": "Ford",
    "model": "Mustang",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# OF CLASS DICT
print(type(thisdict))

#Create DICTS using constructors
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#ACCESSING within dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

#Get Method
x = thisdict.get("model")
print(x)

#Key method
x = thisdict["model"]
print(x)
#Get a list of all the keys with this
x = thisdict.keys()
print(x)

#Adding a new item will also update x
thisdict["month"] = "April"
print(x)

#Getting a list of items
x = thisdict.items()
print(x)

thisdict["month"] = "May"
print(x)

#Update Method:

thisdict.update({"year": 2020})
print(x) #year changes

#LOOP THROUGH A DICTIONARY
for x in thisdict:
    print(x) #loops through a dictionary one by one by KEY NAMES

for x in thisdict:
    print(thisdict[x]) #loops through a dictionary one by one by VALUES

#Looping through both keys and values
for x, y in thisdict.items():
    print(x, ":", y)

#REFERENCE VERSUS COPYING A DICTIONARY (THINK POINTERS)

mydict = thisdict.copy()
print(mydict)



#NESTED DICTIONARIES

#Method 1 nesting all together in one big dictionary
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)


#Method 2: Creating three separate dictionary, then nesting
child1 = {
    "name" : "Emil",
    "year" : 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
    "name" : "Linus",
    "year" : 2011
}

mysecondfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

# Dictionary methods that built-in
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
#

