# Function

#function definition
def sum(a,b): #parameters
    print(a+b)  
    return a + b
    
sum(2,6) #func call , arguments
sum1 = sum(2,8)
print(sum1)

# average of 3
def avg(a,b,c):
    print((a+b+c)/3)
    
avg(2,3,4)

# default parameters
def product(a=2,b=2):
    print(a*b)

product()

# practice
nums = [78,90,57]

# length using function
def checklen(a):
    print(len(a))
checklen(nums)    

# print elements in one line
def numList(a):
    for i in a:
        print(i,end=" ")

numList(nums)
print()

# fictorial
def fic(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print("Fictorial:",f)

fic(4)

# USD to PKR
def moneyConverter(usd):
    pkr = usd*280
    print(pkr,"PKR")

moneyConverter(3)

# Check even odd
def evenOdd(n):
    if n%2==0:
        print("EVEN")
    else:
        print("ODD")
        
evenOdd(6)


# Recursion    #use call stack 
def show(n): 
    if n==0:
        return
    print(n)
    show(n-1)
show(5)

# without using loops print fictorial 
def ficShow(f,fic=1):
    if f==0:
        print(fic)
        return
    fic*=f
    ficShow(f-1,fic)
ficShow(4)
def ficShow1(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* ficShow1(n-1)
    
print(ficShow1(4))

# sum
def sum1(n):
    if n==1:
        return 1
    else:
        return n + sum1(n-1)
print(sum1(5))

marks = ["start",67,68,69,90,"end"]
def showEl(l,i=0):
    if i==len(l):
        return
    else:
        print(l[i])
        showEl(l,i+1)
showEl(marks)