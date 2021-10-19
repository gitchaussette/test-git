
int_list = [1, 2, 3, 4, 6]
float_list = [.1, .2, .3, .4, .5]
almost_number_five_list = [5, 5, 4, 5, 5]
another_list = [8, 4, 45, 45, 6, 5, 45]
another_another_list = [0, 0, -2, 5, 89, 0, -65]

print()

# 3.1.1
def return_sum_from_number_list(list) :
    sum = 0

    for i in list :
        sum += i
    
    return sum

print("Somme de la liste d'Integers : " + str(return_sum_from_number_list(int_list)))
print("Somme de la liste de Floats : " + str(return_sum_from_number_list(float_list)))
print()


# 3.1.2
def return_average_from_number_list(list) :

    average = return_sum_from_number_list(list) / len(list)

    return average

print("Moyenne de la liste d'Integers : " + str(return_average_from_number_list(int_list)))
print()


# 3.1.3
def return_max_element_from_list(list) :
    max_element = list[0]

    for i in list :
        if i >= max_element :
            max_element = i

    return max_element

print("Maximum de la liste d'Integers : " + str(return_max_element_from_list(int_list)))
print()


# 3.1.4
def return_elements_dictionary_from_list(list) :
    elements_dictionary = {}
    index_incrementer = 0

    for i in list :
        elements_dictionary[index_incrementer] = i
        print(elements_dictionary)
        index_incrementer += 1


    return elements_dictionary


# --------- j'ai mis au moins 1h à faire ça mdr ---------
# Ça combine les deux fonctions d'au dessus pour créer une liste
# et attacher les index de TOUS les élément où la valeur est au max.
def return_max_element_indexes_list_from_dictionary(list) :
    elements_dictionary = return_elements_dictionary_from_list(list)
    max_element = return_max_element_from_list(list)
    max_element_indexes_list = []

    for i in elements_dictionary :
        if max_element == elements_dictionary[i] :
            max_element_indexes_list.append(i)

    return max_element_indexes_list


def conjugate_return_max_element_indexes_list_from_dictionary(list) :

    if len(list) == 1 :
        output = "L'index de l'élément maximum de la liste : " + str(return_max_element_indexes_list_from_dictionary(list))
    else :
        output = "Les index de l'élément maximum de la liste : " + str(return_max_element_indexes_list_from_dictionary(list))

    return output


print(conjugate_return_max_element_indexes_list_from_dictionary(another_list))
print()


# 3.1.5
def return_times_character_in_phrase(character, phrase) :
    times_character = 0

    for i in phrase :
        if character == i :
            times_character += 1
    
    return times_character

print("Nombre de fois où le caractère est dans la phrase : " + str(return_times_character_in_phrase("a", "bananananananannanana")))
print()


# 3.1.6
def return_list_elements_states_pos_zero(list) :
    elements_states_list = []

    # J'avais une erreur Index out of Range en utilisant juste
    # for i in list :
    for i in range(0, len(list)) :
        if list[i] > 0 :
            elements_states_list.append(list[i])
        elif list[i] == 0 :
            elements_states_list.append(list[i])

    return elements_states_list

print("Les éléments positifs ou égaux à zéro dans la liste : " + str(return_list_elements_states_pos_zero(another_another_list)))
print()


# 3.1.7
def return_if_list_ascending(list) :
    ascended_list = list.copy()
    ascended_list.sort()

    if ascended_list == list :
        list_state = "est rangée en ordre croissant"
    else :
        list_state = "n'est pas rangée en ordre croissant"


    return list_state

print("La liste " + str(return_if_list_ascending(int_list)))
print()

