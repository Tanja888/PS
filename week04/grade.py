# Reads in a percentage and prints out the grade
# Author: Tanja Juric

x = float(input("Please enter the percentage: "))

if x < 40:
    print ("Fail")
elif x >= 40 and x <= 49:
    print ("Pass")
elif x >= 50 and x <= 59:
    print ("Merit 2")
elif x >= 60 and x <= 69:
    print ("Merit 1")
elif x > 70:
    print ("Distinction")

# other way 

percentage = float (input ("Enter the percentage: "))

if percentage < 0 or percentage > 100: #wrong
    print ("Please enter a number between 0 and 100")
elif percentage < 40:
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit 1")
elif percentage < 70:
    print ("Merit 2")
else:
    print ("Distinction")


