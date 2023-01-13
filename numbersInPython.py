# number in python
x = 1  # int
y = 2.8  # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))

# All integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# All floats
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# All Floats with Es (indicating power of 10)

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers include imaginary numbers
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# CONVERTING Numbers to one another
x = 1
y = 2.8
z = 1j

# converting integer to float
a = float(x)

# converting float to integer
b = int(y)

# convert from integer to complex

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Lets get random
import random

print(random.randrange(1, 10)) #prints random number between 1 and 9 -- Never hits maximum in range

