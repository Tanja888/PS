# Student and courses

# Write a program that stores a student name
# and a list of her courses and grades in dict
# the program should then print out her data
# The numbers of courses she has could change


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
