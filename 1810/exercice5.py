from collections import defaultdict

stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs", 
27.00, "Télévision", 1000, "Cartes mères", "souris", "clavier", 500, "barrettes de mémoire"]

# J'ai trouvé ça ici https://stackoverflow.com/questions/14776980/python-splitting-list-that-contains-strings-and-integers (mais j'ai compris le fonctionnement !)
# defaultdict crée un dictionnaire avec des valeurs par défaut pour les clés
# ici, cela crée un dictionnaire avec pour clés les types de variables Str, Int et Float et elles se rangent comme par magie au bon endroit ! 
# Maintenant je vais aller dormir parce qu'il est 1h du matin
dictionary = defaultdict(list)

print()

# def separate_strings_from_ints(list) :

#     for i in list :
#         dictionary[type(i)].append(i)
#         print(dictionary)

#     print(dictionary[int])
#     print(dictionary[str])
#     print(dictionary[float])

stock_str = []
stock_int = []

for x in stock :
    print(type(x))
    print(type(str(x)))

    if type(x) == type(str(x)) :
        stock_str.append(x)
    
    # elif type(x) == type(int(x)) :
    #     stock_int.append(x)

    else :
        stock_int.append(x)

print(stock_str)
print(stock_int)

# separate_strings_from_ints(stock)

print()

# numbers = []
# first_number = stock[2]
# del stock[2]
# numbers.append(first_number)

# first_number = stock[3]
# del stock[3]
# numbers.append(first_number)

# first_number = stock[4]
# del stock[4]
# numbers.append(first_number)

# first_number = stock[5]
# del stock[5]
# numbers.append(first_number)

# first_number = stock[8]
# del stock[8]
# numbers.append(first_number)

# print()

# print("Tri Chaînes")
# stock.sort(key=str.lower)
# print(stock)
# stock.sort(key=str.lower, reverse=True)
# print(stock)

# print()

# print("Tri Nombres")
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# print()
