# Quiz - Data Structures
# What variable types for each of these?

numberOfQuestions = 5                            # a. numberOfQuestions - integer
averageAge = 23.4                                # b. averageAge - float
debugMode = True                                 # c. debugMode - Boolean
name = "Joe"                                     # d. name - string
ages = []                                        # e. ages - list ? array?
months = ('Jan', 'Feb', 'Mar')                   # f. months - tuple
                                                 # g. months[1] - 'Jan' - string element



book = {}                                        # h. book - dictionary
stuff = [12, 'Fred', False, {}]                  # i. stuff - list (it can store all types of data) ?
                                                 # j. stuff[2] - 'Fred' - item string ? stuff[3] False is Boolean

someone = dict(firstname = "Joe")                # k. someone - dictionary
                                                 # l. someone ["firstname"] - string

me = {                                           # m. me - dictionary
    "firstName" : "Tanja",                       # n. me ["studying"] - list/array (?) nested in a dictionary
    "studying"  : [{                             # o. me ["studying"] [0] ["semester"], semester 1 is integer
        "courseName" : "programming",            # p. me ["studying] [0] ["coursename"], wrong name, it's courseName
        "semester" : 1
    }, {
        "courseName" : "Data Representation",
        "semester" : 2
    }
    ]
}
