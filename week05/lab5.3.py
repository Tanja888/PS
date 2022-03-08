# Random numbers in a list

# Create a program that puts 10 random numbers into a queue (list)
# outputs all the values in the queue
# take the numbers from the queue one at a time
# print that number and the numbers left in the queue
# the command pop(0) takes the first element out of a list

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range (0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print("Queue is {}" .format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print ("Current number is {} and the queue is {}" .format(currentNumber, queue))

print ("The queue is now empty.")

