from random import randint

# Adrián
# Alexandre
# Bastien
# Clément
# Léo
# Quentin
# Romulade

person_list = ("Adrián", "Alexandre", "Bastien", "Clément", "Léo", "Quentin", "Romulade" )

def choose_random_person(tuple) :
    random_number = randint(0, 6)

    chosen_person = tuple[random_number]

    return chosen_person

print(choose_random_person(person_list))