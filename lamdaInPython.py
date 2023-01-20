#lambdaInPython

#Weird looking function
x = lambda a : a + 10
print(x(5))

#adds all numbe
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

#creating a lambda with the return statement
mydouble = myfunc(2) #myfunc returns "lambda a : a * 2"

print(mydouble(11))

#Now you can create multiple uses
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))