# How to read in the modules
# Reading modules until the user enters a module name of blank


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

