# Create a program that allows a user to create new students and to view students
# break into small pieces - use functions

# Write a function that prints out a menu of commands we can perform: add, view and quit
# function should return what the user chose

def displayMenu():
    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()    #cannot see the purpose of this strip yet, looks the same

    return choice

choice = displayMenu()
print ("You chose {}" .format(choice))




'''
student = {
    "name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "grade": 45
        },
        {
            "courseName": "History",
            "grade": 99
        }
    ]
}

print ("Student: {}" .format(student["name"])) 
for module in student["modules"]:
     print("\t {} \t: {}" .format(module["courseName"], module["grade"]))
'''