# OOP
# 4 pillars : Abstraction,Encapsulation,Inheritance,Polymorphism


# Class : blueprint for creating object
# creating class
class Car:
    color = "Blue"
    brand = "Honda"
    
# creating objects
c1 = Car()
print(c1.color, c1.brand)


class Student:
    
    # default constructor
    def __init__(self):  #constructor function
        pass
    
    # parametrized constructor
    def __init__(self, name,marks):  #constructor function
        self.name = name  #different for all objects. (obj attribute)
        self.marks = marks 
        print(f"Adding new student {self.name} in database...")
    university = "Superior" #same for all objects and occupy memory one time (class attribute)
    
    # methods
    def hello(self):
        print("welcome,",self.name)
    def getMarks(self):
        print("Marks:",self.marks)
    
    # static methods
    @staticmethod #decorator
    def check():
        print("hello")

s1 = Student("Affan",90)
s2 = Student("John",85)
print(s1.name, s1.marks, s1.university)
print(s2.name, s2.marks)
s1.hello()
s1.getMarks()
s1.check()

# Abstraction 
class Bike:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Bike started...")
b1 = Bike()
b1.start() #only show essential info

# Practice
# input name and three sub marks then print average
class Average:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.avg = (marks1+marks2+marks3)/3
    def getAvg(self):
        print(f"Name: {self.name} \nAverage: {self.avg}")
s1 = Average("Afan",90,85,80)
s1.name="Affan Shahzad"
s1.getAvg()

# Bank account
class Account:
    def __init__(self,accountNo,balance=500):
        self.accountNo = accountNo
        self.balance = balance
        
    def deposit(self,ammount):
        self.balance+=ammount
        print(f"{ammount} added...")

    def withdraw(self,ammount):
        self.balance-=ammount
        print(f"{ammount} withdrawed...")
       
    def getBalance(self):
        print(f"Account No: {self.accountNo}\nYour balance: {self.balance}") 

a1 = Account(117)
a1.deposit(500)
a1.withdraw(200)
a1.getBalance()