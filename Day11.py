#DAY11
#Copying a List

thislist = ["apple", "banana", "cherry"]
mylist = [] 
mylist= thislist.copy()
print(mylist)

#Using list() method
list1 = ["biryani", "pulao", "nihari"]
new_list = list(list1)
print(list1)

#Using slice operator

cars = ["Toyota", "BMW", "Volvo", "Alto"]
sell = cars[:]
print(sell)