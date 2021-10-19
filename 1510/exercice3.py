stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs", 
27.00, "Télévision", 1000, "Cartes mères", "souris", "clavier", 500, "barrettes de mémoire"]

print(stock)

# GARBAGE #

# listOfStrings = [stock[0], stock[1], stock[3], stock[5], stock[7], stock[9], stock[10], stock[11], stock[13]]
# print(listOfStrings)

# listOfIntegers = [stock[2], stock[4], stock[6], stock[8], stock[12]]
# print(listOfIntegers)

# stringsOfList = ",".join(listOfStrings)

# print(stringsOfList)

# listOfStrings = stock[1::2]
# listOfInts = stock[::2]

# print(listOfStrings)

# GARBAGE #

numbers = []
first_number = stock[2]
del stock[2]
numbers.append(first_number)

first_number = stock[3]
del stock[3]
numbers.append(first_number)

first_number = stock[4]
del stock[4]
numbers.append(first_number)

first_number = stock[5]
del stock[5]
numbers.append(first_number)

first_number = stock[8]
del stock[8]
numbers.append(first_number)

print()

print("Tri Chaînes")
stock.sort(key=str.lower)
print(stock)
stock.sort(key=str.lower, reverse=True)
print(stock)

print()

print("Tri Nombres")
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print()
