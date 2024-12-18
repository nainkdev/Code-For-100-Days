#Day 10 

#To remove specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#To remove by Specified Index
list1 = ["biryani", "pulao", "nihari"]
list1.pop(1)  #It will exclude pulao
print(list1)

list2 = ["Korma", "Sajji", "Dampukht"]
list2.pop()  #This will remove the last item
print(list2)

#The del keyword also removes the specified index:

list3 = ["Mighty burger", "Zinger burger", "Patty Burger"]
del list3[2]
print(list3)

# The del keyword can also delete the list completely.

list3 = ["Mighty burger", "Zinger burger", "Patty Burger"]
del list3
#print(list3) It will generate error as list3 is delete

#Clearing the list

Cars = ["Nissan", "BMW", "lamborgini"]
Cars.clear()
print(Cars)