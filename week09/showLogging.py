# Demonstrate logging
# Attributes you can put into basicConfig
# level
# filename
# filemode
# format
#   %(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)d

import logging
#logging.basicConfig(level=logging.INFO)   #to change the level; it will print everything from an info level and higher
#basicConfig can be run only once
#logging.basicConfig(level=logging.ERROR) #this runs on terminal
logging.basicConfig(filename='debugging.log', #this will create a file not run on a terminal
    filemode='a', 
    level=logging.DEBUG,
    #format='%(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)d')  #s means it's a string, format
    format='%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d')

name = 'joe'

logging.error("This is an error")
logging.critical("Hello")
logging.warning("Whatever %s", name) #placeholder
logging.info("Still going")
logging.debug("and so is this")