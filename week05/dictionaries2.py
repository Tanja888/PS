# Dictionaries 2
# Author: Tanja Juric

car = {
    "make" : "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags" : ["pre-owned", "Best Buy", "Dealer"]
}

#print (car)

for key in car:
    print (key, 'has value', car[key])  #car[key] value of key

# nicer to use items
for key, value in car.items():
    print (key, 'has a value', value)

# make, model, price, tags are keys
