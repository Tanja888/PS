# For Loops
# Author: Tanja Juric

# reads in numbers until 0 is entered
# it will print out the numbers in a list and their average

numbers = []

number = int(input("Enter number (0 to quit): "))
while number != 0:
    numbers.append(number)

    number = int(input ("Enter another (0 to quit): "))

for value in numbers:
    print (value)

average = float (sum(numbers) / len(numbers))
print ("The average is {}" .format(average))






