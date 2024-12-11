#Booleans only consist of True and False

a = True
print (type(a))

my_str = "Hassnain123"
my_str1 = "Hassnain"
   
print( my_str.isalnum())
print(my_str1.isalpha())    
print("1234".isdigit())    
print(my_str.istitle())
print("HASSNAIN".isupper())
print("abc".islower())
print(" ".isspace())
print(my_str1.endswith('n'))
print(my_str.startswith('H'))

#Booleans Operation 
#Both condition should be true
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#One condtion must be true

print(True or True)
print(True or False)
print(False or True)
print(False or False)


print(my_str1.endswith('n') or my_str.startswith('L'))
print(my_str1.endswith('n') and my_str.startswith('L'))

