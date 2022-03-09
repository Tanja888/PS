# Create a new menu item called save; use students program from week6
# when the user selects the doSave() function should be called

students = []

def displayMenu():

    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q):").strip()   
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent ["name"] = input("Enter name: ")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input ("\tEnter the first Module name (blank to quit): ").strip() 

    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        module ["grade"] = int(input("\tEnter grade: "))
        modules.append(module)
        moduleName = input ("\tEnter the next Module name (blank to quit): ").strip()
    
    return modules


def displayModules (modules):
    print("\tName  \t\tGrade")
    for module in modules:
        print("\t{} \t{}" .format(module["name"], module["grade"]))


def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])


def doSave(students):
    print("In save")


# It will not print anything until we add the main program
students = []
choice = displayMenu()
while (choice != 'q'):          # could use lambda function instead
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice !='q':
        print ("\n\nPlease select either a, v, s or q")
    choice = displayMenu()