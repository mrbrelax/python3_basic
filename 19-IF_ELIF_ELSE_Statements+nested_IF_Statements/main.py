# IF..ELIF..ELSE Statements + nested IF Statements
x = 10
if x >= 0:
    print("x is positive")
    if (x%2) == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is negative")

name = input("Enter a name : ")

if name == "Max":
    print("Name entered is : ", name)
elif name == "Leo":
    print("Nama entered is : ", name)
elif name == "Roy":
    print("Nama entered is : ", name)
elif name == "Eli":
    print("Nama entered is : ", name)
else:
    print("The Name entered is invalid")
