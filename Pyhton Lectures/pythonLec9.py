# OOP
# 4 pillars : Abstraction,Encapsulation,Inheritance,Polymorphism
# last two pillars

# del keyword : used to delete object properties or object itself

class Student:
    def __init__(self, name,rollNo):
        self.name = name
        self.rollNo = rollNo

s1 = Student("Affan",26)

print(s1.name,s1.rollNo)
del s1.rollNo
# print(s1.name,s1.rollNo)

# private(like) attrributes and methods :not accesible outside the class 
class Account:
    def __init__(self, accNo,accPass):
        self.accNo = accNo
        self.__accPass = accPass #private __ is used for private data
    
    def resetPass(self):
        print("previous Pass:",self.__accPass)

s1 = Account(117,3517)

print(s1.accNo) #accessible
# print(s1.__accPass) #not accessible

s1.resetPass()

class Person:
    __name = "Afan"
    
    def __hello(self):
        print("Hello user:",self.__name)
        
    def welcome(self):
        self.__hello()

p1 = Person()

# p1.__hello() #Not accessible
p1.welcome()

# Inheritance : When one class(child) inherits the properties and methods of another class(parent)
# Types of Inheritance : Single, Multi-level, Multiple

# Single
class Car:     
    @staticmethod
    def start():
        print("Car started...")
        
    @staticmethod
    def stop():
        print("Car stopped...")

class LuxuryCar(Car):
    
    def __init__(self, brand):
        self.brand = brand
    
car1 = LuxuryCar("Furtuner")
car2 = LuxuryCar("G wagon")

print(car1.brand)
car1.start()
    
# Multi-level 
class Fortuner(LuxuryCar):
    def __init__(self, type):
        self.type = type
    
car1 = Fortuner("diesel")
print(car1.type)
car1.start()

# Multiple 
class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A, B):
    varC = "Welcome to class C"
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# Super method : used to access methods of the parent class

class Bike:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Bike started...")
        
    @staticmethod
    def stop():
        print("Bike stopped...")
        
class ToyotaBike(Bike):
    def __init__(self, name, type):
        super().__init__(type) #call the constructor of parent class
        self.name = name
        super().start()
    
bike1 = ToyotaBike("Honda", "electric")
print(bike1.type)

# class method : bound to class and receives the class as an implicit first argument 
# Note : static method can't access or modify class state and generally for utility

class User:
    name = "Unknown"
    def changeName(self, name):
        self.name = name #changes the object attribute not class attribute
        # User.name = name #1st method
        # self.__class__.name = name #2nd method
        
    # direct method (3rd method) 
    @classmethod
    def changeName1(cls, name):
        cls.name = name #changes the class attribute not object attribute
        
p1 = User()
p1.changeName("Affan")
print(p1.name)
print(User.name)
p1.changeName1("John")
print(p1.name)
print(User.name)

# Property method : use the method as a property
class Student1:
    def __init__(self, phy, chem, eng):
        self.phy = phy
        self.chem = chem
        self.eng = eng
        # self.percentage = str((self.phy + self.chem + self.eng) / 3) + "%"
    
    # def calPercentage(self): #one method
    #     self.percentage = str((self.phy + self.chem + self.eng) / 3) + "%"
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.eng) / 3) + "%"

s1 = Student1(85, 90, 95)
print(s1.percentage)

s1.phy = 98
print(s1.phy)
print(s1.percentage)

# Polymorphism : operator overloading (When the same operator is allowed to have diff meaning)
print(1+2)
print("Hello " + "Affan") #concatenate
print([1,2,3] + [4,5,6]) #merge

# add complex numbers
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNo(self):
        print(self.real,"i +",self.img,"j")
        
    def addNo(self, realNo, imgNo):
        print(self.real + realNo,"i +",self.img + imgNo,"j")
        
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        # print(newReal,"i +",newImg,"j")
        
    # using Dunder functions
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

        
num1 = Complex(5, 12)
num1.showNo()
num2 = Complex(3, 8)
num2.showNo()

num1.addNo(3, 8)

num3 = num1.add(num2)
num3.showNo()

print("Using dunder function")
num3 = num1 + num2
num3.showNo()

num3 = num1 - num2
num3.showNo()

# practice
# calc Area and perimeter using radius
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return round(math.pi*self.radius**2,2)
    
    @property
    def perimeter(self):
        return round(2*math.pi*self.radius,2)

    
c1 = Circle(4)
print(c1.area)
print(c1.perimeter)

# inheritance practice
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self, name=None, age=None):
        if name and age:
            print("Name:", name)
            print("Age:", age)
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)
    
e1 = Employee("Stutent", "BSCS", 30000)
# e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        Engineer.name = name
        Engineer.age = age
        super().__init__("Engineer", "CS", 30000)
    def showDetails(self):    
        super().showDetails(self.name, self.age)

eng1 = Engineer("Afan", 20)
eng1.showDetails()

# store items and prices use dunder function __gt__ to convey that: order1>order2 if price1>price2
class Order(object):
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, odr2):
        return self.price > odr2.price
    
    
odr1 = Order("Cock", 150)
odr2 = Order("Lays", 50)
    
print(odr1 > odr2)