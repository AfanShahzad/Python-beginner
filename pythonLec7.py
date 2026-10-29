# File I/O

# r: reading (default)
# w: writing,truncating the file first (overwrite all file)
# x: create new file and open for writing
# a: open for writing,appending to the end of the file if exists
# b: binary mode
# t: text mode (default)
# +: open a disk file for updating (reading & writing)


# open
f = open("demo.txt","r") #(file path or name, mode)

# data = f.read() #read whole file
# print(data)
# data2 = f.read(5) #range
# print(data2)

print("Line 1")
line1 = f.readline()
print(line1)
print("Line 2")
line2 = f.readline()
print(line2)

f.close()

# write
f = open("demo.txt","w")

f.write("this is lecture 7 demo text file")

f.close()

# append
f = open("demo.txt","a")

f.write("\nHello i am Affan.")

f.close()

# read write, but overwrite
f = open("demo.txt","r+")
print("r+\n",f.read())
f.write("heay")

f.close()

# read write but truncate
f = open("demo.txt","w+")
print("w+",f.read())
f.write("Hello i am Affan.")

f.close()

# read and write but stream is positioned at the end of file 
f = open("demo.txt","a+")
print("a+",f.read())
f.write("\nthis is lecture 7 demo text file")

f.close()

# with syntax: no need to close the file 
with open("demo.txt","r") as f:
    data = f.read()
    print(data)
    
# Deleting file 
# using the os module   #extra info :to install any module -> pip install tensorflow
with open("demo2.txt","w") as f:
    f.write("Helloo")
import os

os.remove("demo2.txt")

# practice 
# create and write in file
with open("demo2.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java\ni like programming in java")
    
# replace all occurances of java with Python
with open("demo2.txt","r") as f:
    data = f.read()
    
newData = data.replace("java","Python")
print(newData)

with open("demo2.txt","w") as f:
    f.write(newData)
    
# Search if learning exists
with open("demo2.txt","r") as f:
    data = f.read()
    if (data.find("learning")!= -1):
        print("Found")
    else:
        print("Not found")
        
def checkForLine():
     
    data = True
    lineNo = 1
    with open("demo2.txt","r") as f:
        while data:
            data = f.readline()
            if ("learning" in data):
                return f"Found on line: {lineNo}"
            lineNo+=1
        else:
            return -1

print(checkForLine())

def checkEven():
    
    with open("demo3.txt","w") as f:
        f.write("1, 2, 76, 90, 101")
    with open("demo3.txt","r") as f:
        data = f.read()
        # manual method
        # num=""
        # for i in data:
        #     if (i==","):
        #         print(int(num))
        #         num=""
        #     else:
        #         num+= i
        # else:
        #     print(int(num))
        
        # builtin method
        count = 0
        splitdata = data.split(", ")
        print(splitdata)
        
        for i in splitdata:
            if int(i)%2==0:
                count+=1
    print(count)
        
    
checkEven()


