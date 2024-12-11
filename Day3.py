#LISTS
mylist = ["apple", "banana", "cherry"]
print(mylist)
# for finding length

print(len(mylist))

#for finding type of list

print(type(mylist))

#list constructor

New_list = list(("Orange", "Berry", "Mango"))
print(New_list)

#For Accessing List Items 

print(New_list[1])  #indexing starts from 0
print(New_list[-1]) #Negative indexing means start from the end (-1 refers to the last item,)

#Range of List
 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print (thislist[:]) #For printing every item

print (thislist[2:5]) #The search will start at index 2 (included) and end at index 5 (not included).

print(thislist[:4]) #it will print from first item to the 4th

print(thislist[2:]) #includes from cherry to the lasts

#Check if Item Exists

if "apple" in thislist:
      print("Yes, 'apple' is in the fruits list")