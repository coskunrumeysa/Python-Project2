# Firstly, introduce who (programmer) write this program.
__author__ = "Rümeysa Coskun - Computer Engineer && Software Engineer"

# These program write for a cafe menu.

print("-----------> Welcome To The Pati Cafe <-----------")

# Menu
print("<<<<<<<<<<< Menu <<<<<<<<<<<<<<<")
print("Food      ------1")
print("Drinks    ------2")
print("Desserts  -------3")

choice = input("Please enter your cohoice:")
name = input("Please enter your name:")

if choice == "1":
    print("Your choice is : Food dear", name)

elif choice == "2":
    print("Your choice is : Drink dear", name)

elif choice == "3":
    print("Your choice is : Desserts dear", name)

else:
    print("Invalid choice dear", name)

