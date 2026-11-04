# - Dictionary : stores data values in key:value pair
# - Sets

# Dictionary
data = {
    "name":"Afan",
    "age":19,
    "marks":"95%",
    "isAdult": True,
    "subjects": ["Python","C","Java"]
}
print(data)
data["age"] = 20
print(data["age"])

# Nested Dictionary
student = {
    "name":"Afan",
    "age": 20,
    "marks":{
        "math": 90,
        "eng": 80,
        "phy": 95,
    }
}
print(student)
print(student["marks"]["math"])

# Dict methods
print(student.keys())
print(list(student.keys())) #type cast to list
print(student.values())
print(list(student.values())) #type cast to list
print(student.items())
pairs = list(student.items())
print(pairs[0])
print(student.get("name")) #same as student["name"] but get fun gives "none" instead of error
student.update({"city":"Sargodha"})
print(student)

# Sets:collection of unordered unique values
nums = {1,2,2,3,4,"Afan"}
print(nums)
num = set() #syntax for emty sets

# set methods
num.add(1)
num.add(2)
num.add("Hello")
num.add("world")
num.remove("world")
# num.pop() #removes randomly
# num.clear()
print(num)

print("union" , num.union(nums))
print("Intersection", num.intersection(nums))


# Practice
# 1. store word meanings in dict
eng={
    "Cat": "A cute animal",
    "Mango": ["A fruit","Chonsa"]
}
print(eng)

# 2. How MANY classrooms are required for each subject given below:
# "Python","Java","C++","Python","Javascript","Java","Python","C++","C"
subjects = {"Python","Java","C++","Python","Javascript","Java","Python","C++","C"}
print("Required Classrooms:", len(subjects))

# 3. input from user subject and marks in pair
data1={}
# sub1 = input("Enter subject 1:")
# mark1 = input("Enter marks:")
# data1[sub1]=mark1
# sub1 = input("Enter subject 2:")
# mark1 = input("Enter marks:")
# data1[sub1]=mark1
# sub1 = input("Enter subject 3:")
# mark1 = input("Enter marks:")
# data1[sub1]=mark1
print(data1)

# 4.store 9 and 9.0 in set
num1={9,"9.0"}
print(num1)