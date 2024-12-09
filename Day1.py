# DAY-1 (BASICS)
print("Hello World")

# Operations
print(50+50)   #Addition
print(35-15)   #Minus
print(40/2)   #Divide
print(50%5)   #Reminder 

# Variables 
a = 50   
b = "Hello There"
c = 53.5   
d = True    

# Datatypes
a1 = 50   #Integers
b1 = "Hello There"  #Strings
c1 = 53.5   #Floats
d1 = True    #Boolean
f = 5j #Complex

x1 = ["apple", "banana", "cherry"]	#list	
x2 = ("apple", "banana", "cherry")	#tuple	
x3 = range(6)	#range	
x4 = {"name" : "John", "age" : 36}	#dict	
x5 = {"apple", "banana", "cherry"}	#set
print(a1,b1,c1,d1)

#Finding the type 
print (type(a1))
print (type(b1))
print (type(c1))
print (type(d1))

#Unpacked collection 

fruit = ["Orange","Apple","Mangos"] 
x,y,z = fruit
print(x,y,z)

# global-var
x = "Awesome"

def myfunc() :
    print ("python is " + x)

myfunc()

#Conversion of datatypes
x =100
y= 50.5
z= 144j

a= float(x)
b= complex(y)
print(a,b)

#importing random numb library library

import random 
print(random.randrange(1,10))
