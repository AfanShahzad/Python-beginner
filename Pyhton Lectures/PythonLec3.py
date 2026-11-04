# Lists : stores elements of different types
# Tuples


# Lists
marks = [69,89,78]
print(marks)
print(marks[1])

data = ["Afan",26,90.0] #diff types allowed
data[2] = 98 #Mutable
print(data)


# List slicing : similar to str slicing
data = ["Afan",26,90.0,"Pakistan"]
print(data[1:3])
print(data[1:])
print(data[-3:-1])

# List methods
# data.sort()  #can't sort both int and str together
# data.sort(r"BSCS"everse=True) #desending order
data.append(20)
data.insert(2,"BSCS")
data.remove(90.0)
data.pop()
print(data)


# Tuples : immutable sequence of values
tup = (4,9,2,4,2)
print(tup)
print(tup[1])
print(tup[1:3])
print(tup.index(4))
print(tup.count(4))

# Practice 
# 1. store names in list
data=[]
name1="Afan"
name2="Changu"
name3="Jon"
data.append(name1)
data.append(name2)
data.append(name3)
print(data)

# 1. checks palindrome  :e.g ma'am
data=[1,2,2,1]
data2=[1,2,3,1]
dataCopy=data.copy()
dataCopy.reverse()
if data==dataCopy:
    print(True)
else:
    print(False)
    
# 2. number of grade A
tup=("A","B","B","A","A","D")
print(tup.count("A"))
# 3. sort the grades
grade=["A","B","B","A","A","D"]
grade.sort()
print(grade)


