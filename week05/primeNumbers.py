# Lists to generate prime numbers
# Author: Tanja Juric
# How to add things into a list and iterate through it

primes = []

for candidate in range (2, 101):
    #print (candidate)
    isPrime = True
    for divisor in range (2, candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break

    if isPrime:
        primes.append(candidate)

print (primes)


#shorter way:

primes = []
upto = 100000 #better to put variables than values

for candidate in range (2, upto):
    #print (candidate)
    isPrime = True
    # this way only checks if the number is divisible by prime
    for divisor in primes:
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # there is no reason to keep checking if it is not divisible by an int
            break

    if isPrime:
        primes.append(candidate)

print (primes)