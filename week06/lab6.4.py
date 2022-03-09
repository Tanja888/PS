# Write the function doAdd (students)
# a. Read in a student's name
# b. Read in the module names and grades (separate function)
# c. test the function, it creates a student dict, we can print it out
# d. add the student dict to list (pass this list in)
# e. test it


students = []
def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter name: ")
    currentStudent ["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
print(students)

