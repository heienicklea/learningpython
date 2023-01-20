#classesInPython

class MyClass:
    x = 5


#THIS IS AN OBJECT NAMED P1 of CLASS MyClass
p1 = MyClass()
print(p1.x)


#Creating a class of what describes person
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#this is a new object named p1 of class person named john and of age 36
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(p1) #without string function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}++++({self.age})"

p1 = Person("John", 36)

print(p1) # With string functions

print("____________________________________")

#OBJECT METHODS

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#MODIFYING OBJECTS

p1.age = 40 #adding age

del p1.age #deleting age

p1.myfunc() #still knows John, os can run the function

del p1.name

#p1.myfunc() this is an error because name is gone

#Inheritance of Classes


#THIS IS PADRE
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#lets say you wanted to add stuff to student class

class Student(Person):
  def __init__(self, fname, lname):
      self.graduationyear = 2019
      #add properties etc.

#HOWEVER, this would override everything done before in the person class
#to keep the init before (CALL THE PERSON CLASS
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

#THIS WILL alow you inherit all the methods and properities from its parents (making it the same plus whatever is added)
class Student(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = 2019

    def printgraduationyear(self):
        print(self.graduationyear)

x = Student("Mike", "Olsen", 2019)

x.printgraduationyear()