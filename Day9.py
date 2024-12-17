#Day 9 
# Append Items (Adding items)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Using Extend()To append elements from another list to the current list,
list1 = ["biryani", "pulao", "nihari"]
fastfoods = ["Burger", "pizza", "french fries"]

list1.extend(fastfoods)
print(list1)

#Adding two lists using + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)