# different way of dealing with the user's choice


def displayMenu():
    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()   
    return choice

def doAdd(students):
    print("do add")
def doView(students):
    print("do View")
def doNothing(dumby):
    pass

#dict that maps a letter to the function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing
}

students = []
choice = displayMenu()
while (choice != 'q'):
    if choice in choiceMap:
        choiceMap[choice](students)
    else:
        print("\n\nPlease select either a,v or q")
    
    choice = displayMenu()

