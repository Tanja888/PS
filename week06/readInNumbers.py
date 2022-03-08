# Try to write a function
# Author: Tanja Juric

"""
num1 = False
while (num1 == False):
    try:
        num1 = int(input("Enter a number: "))
    except ValueError:
        print ("That was not a number, ", end="")

num2 = False
while (num2 == False):
    try:
        num2 = int(input("another: "))
    except ValueError:
        print ("That was not a number, ", end="")

#num2 = int(input("And another: "))

answer = num1 * num2

print(f"Answer is {answer}")
"""

# Create a function instead
def readNum (message = "Enter a number: "):
    num = False  
    while (not num):            #(not num) is nicer than num == False
        try:
            num = int(input(message))
        except ValueError:
            print ("That was not a number, ", end="")
    return num

num1 = readNum()
num2 = readNum("Enter the second number: ")

answer = num1 * num2

print(f"Answer is {answer}")

  