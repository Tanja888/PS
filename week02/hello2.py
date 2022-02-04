# Another attempt of printing person's name
# Author: Tanja Juric

# If I don't put space after : my name will be attached to the rest of the text
name = input ('Enter your name: ')
print ('Hello {}\nNice to meet you.' .format(name))

print ('Hello ' + name + '\nNice to meet you.')