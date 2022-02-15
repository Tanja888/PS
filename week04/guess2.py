# Guessing the number with if, too high and too low number
# Author: Tanja Juric

numberToGuess = 22

# if statement inside the while loop
guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too low")
    else: 
        print ("Too high") #It can't be equal or too low, it can only be too high
    guess = int(input("Please guess again: "))

print ("Well done! Yes, the number was", numberToGuess)