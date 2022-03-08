# Dictionaries
# Author: Tanja Juric

car = {
    "make" : "ford",
    "model" : "modeo",
    "year" : 2006,
    #"owner" : "Andrew",
    #"owner-driver-number" : 1234
    
    #dictionary object owner inside dictionary object car
    "owner" : {
        "name" : "Andrew",
        "driver-number": 1234
    }
}

#attr = "make"
#print (car["owner-driver-number"]) #made a variable but can also do without - print(car["year"])

print(car["year"])
#print (car["owner"]["name"])
print(car["owner"].get("names")) #names instead of name - it will return None, not an error
print (type(car["owner"].get("names"))) #get if we don't know if something exists or not



