# strings : stores a sequence of characters
# conditional statements



# escape seq char \n \t
str1="this is a string. \ncreating in python" 
print(str1)

# concatenation
str1="hello"
str2="world"
print(str1 + str2)

# length
print(len(str1))

# indexing: we can access not edit
str1="hello"
print(str1[0])

# slicing
str1="hello"
print(str1[1:4])
print(str1[1:]) #empty value is same as len(str1)
# negative slicing
print(str1[-4:-1])


# str some functions
str1="hello world"
print(str1.endswith("world"))
print(str1.capitalize())
print(str1.replace("world","changu"))
print(str1.find("world"))
print(str1.count("l"))


# practice
# 1 input name and print length of name
# name = str(input("Enter name: "))
# print(len(name))
# 2 find the occurence of $ in str
msg="1 have 10$ and my friend has 20$."
print("count: ",msg.count("$"))


# conditional statement: if-else-if
light = "green"
if(light=="green"):
    print("Go")
elif(light=="red"):
    print("Stop")
else:
    print("look")
# grade example
marks=80
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>60:
    print("D")
else:
    print("F")    
    
# nesting
age=20
if age>18:
    if age>=80:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")
    

# practice
# 1. Check if number is E or O
# num = int(input("Enter number: "))
num=4
if num%2==0:
    print("Even")
else:
    print("Odd")   

# 2. find greater number
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
num1=5
num2=10
num3=7
if (num1>num2)and(num1>num3):
    print("Num: ",num1)     
elif (num2>num1)and(num2>num3):
    print("Num: ",num2)     
else:
    print("Num: ",num3)     
    
# 3. find greater number
num1=28
if num1%7==0:
    print("Multiple of 7")
else:
    print("Not a multiple") 