#forLoopsInPython

fruits = ["apple", "banana", "cherry"]

#Looping through a list
for x in fruits:
    print(x)

#looping through a word
for x in "banana":
    print(x)

#break statement to stop midway through a for loop

for x in fruits:
    print(x) #prints apple and banane, not cherry
    if x == "banana":
        break

print("______")

#break statement is before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #only prints apple


#range functions returns a sequence of numbers and ending at specified number (Meaning does not print 6)
for x in range(6):
    print(x)

print("__________")

#Make a range between 2 and 30, and increment by 3
for x in range(2, 30, 3):
  print(x)


#NESTED LOOPS

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


#Print 3 * 3 = 9
for x in adj:
  for y in fruits:
    print(x, y)

