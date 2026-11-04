# Loops 

# while loops

# 1 to 10 print
a = 1
while a<=10:
    print(a)
    a+=1
    
# table
a = 1
b = 2
while a<=10:
    print(f"{b}x{a}={a*b}")
    a+=1
    
# print elements of list
num = [1,2,6,3,76,9,6]
i=0
while i<len(num):
    print(num[i])
    i+=1
    
# search 6 in list
i = 0
isAvailable=False
while i<len(num):
    if num[i]==6:
        print("Found at index",i)  
        isAvailable = True
    i+=1
if not isAvailable:
    print("not found")
    
# Break and Continue
i=1
while i<=5:
    print(i)
    if i==3:
        break
    i+=1

i=1
while i<=5:
    if i==3:
        i+=1
        continue #skips the print in this iteration 
    print(i)
    i+=1
    
# for loops : sequential traversal for list string tuples etc
for el in num:
    print("ELemnt",el)

name = "Afan"
for ch in name:
    if ch=="f":
        print(ch,"found")
        break
    print(ch)
else:
    print("end")
    
# range()
for i in range(5):
    print(i)
for i in range(2,11,2): #(start,stop,step)
    print(">",i)
    
# table
for i in range(1,11):
    print(f"2x{i}={2*i}")

# pass
for i in range(5):
    pass #skip for the future use(null statement)

# sum of first n numbers with while
i=1
sum=0
while i<=5:
    sum+=i
    i+=1
print(sum)

# fictorial
x=4
f=1

for i in range(1,x+1):
    f*=i
    print(f)
    
