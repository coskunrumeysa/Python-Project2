# Firstly , introduce  who written this program.
__author__ = "Rumeysa Coskun - Computer Engineer && Software Engineer"

# These code examples for variables.
# Variable : Names of value in the program. Variables are changeable . These variables hold on the Ram. And can do some
# operations with these variables.

# Numerical Variables
# 1-Integer
# 2- Float
# 3- Character Variable
# 4- Character string
# Integer
# These code block a variable : X and value of this variable 3. And we want learn type of this variable with type() function
#And print the screen of type variable.
x = 3
print(type(x))
print(5*x)

# Float
# These code block a variable : pi and value of this variable 3.14 . And we want learn  type of this variable with type() function
# And print the screen of type variable.
pi=3.14
print(type(pi))

print("Result is:", pi*x)

# Character Variable
engineer ="r"
print(type(engineer))
print(len(engineer))
print(engineer)

# Character String
username="rumeysa coskun"
password="rum"

print(type(username))
print(type(password))

print(len(username))
print(len(password))

print(len(username)+len(password))

print(username+password)

# Function Decleration
# Fİrstly , function name then paranteshesis then : symbol

def bat_giris(ad,soyad,sistem,il) :
    print("-"*20)

    print("Please enter the name:" , ad)
    print("Please enter the surname:", soyad)
    print("Please enter system :" , sistem)
    print("Please enter the city:", il)

    print("-" * 20)

bat_giris("rumeysa","coskun","bat","istanbul")






