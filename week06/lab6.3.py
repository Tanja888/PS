# Create a program that keeps displaying the menu until the user picks q
# If the user picks a then call a function called doAdd()
# If the user picks v call a function doView()

def displayMenu():
    print ("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()   
    return choice
def doAdd():
    print("in adding")
def doView():
    print("in viewing")

choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q':
        print ("\n\nPlease select either a, v or q")
    choice = displayMenu()




#print ("You chose {}" .format(choice))
