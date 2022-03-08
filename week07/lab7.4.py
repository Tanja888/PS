# Read in a dict object from a file (with load - from a file)
# Author: Tanja Juric

import json
filename = "testdict.json"

def readDict():
    with open(filename) as f:
        return json.load(f)

somedict = readDict()
print(somedict)