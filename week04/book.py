# Automate the Boring Stuff with Python

#spam = 0
#if spam < 5:
    #print ("Hello, World.")
    #spam = spam + 1

spam = 0
while spam < 5:
    print ("Hello, World")
    spam = spam + 1

#name = ''
#while name != 'your name':
    #print ('Please type your name: ')
    #name = input()
#print ('Thank you')

while True:
    print ('Please type your name')
    name = input()
    if name == 'your name':
        break
print ('Thank you')
