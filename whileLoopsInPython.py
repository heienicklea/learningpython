#whileLoopsInPython


i = 1

while i < 6:
    print(i)
    i += 1


#BREAKS
i = 1
while i < 6:
    print(i)
    if i == 3:
        break # can break while loops inside the loop even if the condition is true
    i += 1


#CONTINUES
i = 0

while i < 6:
    i += 1
    if i ==3:
        continue #continues onto the next loops and stop the current iteration (For this example, it wont print 3)
    print(i)

i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6") #Sort of is a 'final statement' - as soon as the while statement is false it runs




