#ifElseInPython

#CONDITIONALS AND IF STATEMENTS

# LOGICS FROM MATHS:
# Equals: a == b
# Not Equals: a != b
# Less Than: a < b
# Less Than or Equal To: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200

if b > a:
    print("b is greater than a") #notice indentation on python


if b < a:
    print("b is less than a")
elif a > b: #added conditional
    print("a is greater than b")
else: #added action if everything fails
    print("A and B is the same")

#Short code if desired (prints b if a is not greatre than b
print("A") if a > b else print("B")


if b > a:
    pass #can be used if you have no content for the if statement, and want to avoid error
