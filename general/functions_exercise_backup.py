
# ex 1.5.1
def return_number_state_pos_zero_neg(number) :
    number_state = ""

    if number > 0 :
        number_state = "positif."

    elif number == 0 :
        number_state = "égal à zéro."

    else :
        number_state = "négatif."

    output = "Le nombre est " + number_state

    return output


# ex 1.5.2
def return_number_state_even_odd(number) :
    number_state = ""

    if number % 2 == 0 :
        number_state = "pair."

    else :
        number_state = "impair."

    output = "Le nombre est " + number_state

    return output


# ex 1.5.3
def return_smaller_number(number1, number2) :
    smaller_number = ""

    if number1 < number2 :
        smaller_number = str(number1)

    else :
        smaller_number = str(number2)

    output = "Le nombre le plus petit est : " + smaller_number

    return output


# ex 1.5.4
def return_smaller_or_greater_number(number1, number2, number3):
    smaller_number = ""
    greater_number = ""

    if number1 < number2 and number1 < number3 :
        smaller_number = str(number1)

    elif number2 < number1 and number2 < number3 :
        smaller_number = str(number2)

    else:
        smaller_number = str(number3)


    if number1 > number2 and number1 > number3 :
        greater_number = str(number1)

    elif number2 > number1 and number2 > number3 :
        greater_number = str(number2)

    else:
        greater_number = str(number3)

    output = ("Le nombre le plus petit est : " + smaller_number
    + "\nLe nombre le plus grand est : " + greater_number)

    return output


# ex 1.5.5
def return_week_message(day) :
    message = ""

    if day == "lundi" :
        message = "C'est reparti !"

    elif day == "mardi" or day == "jeudi" :
        message = "Bonne semaine ;)"

    elif day == "mercredi" :
        message = "Jour des enfants."

    elif day == "vendredi" :
        message = "Bientôt le week-end !"

    elif day == "samedi" or day == "dimanche" :
        message = "Bon week-end <3"

    else :
        message = "C'est pas un jour de la semaine, ça ! >:("

    return message


# ex 1.5.6
def return_color_type(color) :
    color_type = ""

    if color == "rouge magenta" or color == "bleu cyan" or color == "jaune" :
        color_type = "Couleurs primaires."

    elif color == "orange" or color == "violet" or color == "vert" :
        color_type = "Couleurs secondaires."

    else :
        color_type = "Autres couleurs."

    return color_type


# ex 1.6
def return_strange_calculation(x) :

    if x % 9 == 0 :
        y = x / 9

    else :
        y = x - 9

    output = "y = " + str(y)

    return output


# ex 1.7
def return_price_per_person_for_group(nb_persons) :

    if nb_persons >= 5:
        p = 700 + 170*nb_persons

    else :
        p = 700 + 210*nb_persons

    output = ("Prix par personne : " + str((p/nb_persons)) 
    + " €, pour un groupe de " + str(nb_persons) + " personnes.")

    return output


# ex 1.8
def ask_yes_no_get_length() :
    user_input = input("Répondre oui ou non : ")
    answer = ""

    if user_input == "oui" or user_input == "non" :
        answer = "La réponse est " + user_input + "."

    else :
        answer = "C'est une mauvaise réponse."

    if len(user_input) == 3 :
        length_answer = "La réponse est constituée de trois caractères."

    else :
        length_answer = "La réponse n'est pas constituée de trois caractères."

    output = "La réponse est : " + answer + "\n" + length_answer

    return output


# ex 2.1.1
def ask_user_name_say_hello() :
    user_name = input("Entrez un prénom : ")

    output = "Bonjour, " + user_name + " !"
    return output


# ex 2.1.2
def ask_birthyear_return_age(currentYear) :

    while True :
        try :
            birthyear = input("Entrez votre année de naissance : ")
            age = currentYear - int(birthyear)
            break
        except :
            print("C'est des chiffres qu'il faut écrire ! >:(")

    if age < 0 :
        output = "Vous venez du futur ?! :o"
    else :
        output = "Vous avez " + str(age) + " ans."

    return output


# ex 2.2.1, 2.2.2, 2.2.3
def return_week_days_list_operations() :
    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    output = "La Liste des jours de la semaine : " + str(weekDays) + \
    "\nLe jour à l'index 4 de la Liste : " + str(weekDays[4]) + "."

    weekDays.reverse()

    output_after_reverse = "La Liste des jours de la semaine, inversée : " + str(weekDays)

    return output + "\n" + output_after_reverse


# ex 2.3
def return_stock_list_operations() :
    stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Haut-parleurs", 
    27.00, "Télévision", 1000, "Cartes mères", "souris", "clavier", 500, "barrettes de mémoire"]

    output_stock_before = "La Liste stock : " + str(stock)

    # Opérations de séparation des Integers et des Strings
    # Les Integers se retrouvent dans la Liste stock_integers
    # Les Strings restent dans stock
    stock_integers = []
    current_int = stock[2]
    del stock[2]
    stock_integers.append(current_int)

    current_int = stock[3]
    del stock[3]
    stock_integers.append(current_int)

    current_int = stock[4]
    del stock[4]
    stock_integers.append(current_int)

    current_int = stock[5]
    del stock[5]
    stock_integers.append(current_int)

    current_int = stock[8]
    del stock[8]
    stock_integers.append(current_int)


    stock.sort(key=str.lower)
    output_strings_sorted = "Tri des Strings : " + str(stock)

    stock.sort(key=str.lower, reverse=True)
    output_string_sorted_reversed = "Tri des Strings, inversé : " + str(stock)

    stock_integers.sort()
    output_integers_sorted = "Tri des Integers : " + str(stock_integers)

    stock_integers.sort(reverse=True)
    output_integers_sorted_reversed = "Tri des Integers, inversé : " + str(stock_integers)

    return (output_stock_before + "\n" + output_strings_sorted + "\n" + output_string_sorted_reversed 
    + "\n" + output_integers_sorted + "\n" + output_integers_sorted_reversed)


# ex 2.4
def return_num_alpha_operations() :
    numList = [1,2,3,4,5]
    alphaList = ["a","b","c","d","e"]

    output_before_list_assignation = str(numList is alphaList) + "\n" + str(numList == alphaList)

    numList = alphaList

    output_after_list_assignation = "\n" + str(numList is alphaList) + "\n" + str(numList == alphaList)

    return output_before_list_assignation + output_after_list_assignation


# ex 2.5
def return_many_list_operations() :
    list = [17, 38, 10, 25, 72]

    list.sort()
    first_output = "La Liste triée : " + str(list)

    list.append(12)
    second_output = "La Liste avec un élément en plus : " + str(list)

    list.reverse()
    third_output = "la Liste, inversée : " + str(list)
    fourth_output = "L'index de l'élément égal à 17 : " + str(list.index(17))

    list.remove(38)
    fifth_output = "La Liste, sans l'élément égal à 38 : " + str(list)
    sixth_output = "La Liste du deuxième au troisième élément : " + str(list[1:3])
    seventh_output = "La Liste du premier au deuxième élément : " + str(list[:2])
    eighth_output = "La Liste du troisième au dernier élément : " + str(list[2:])
    ninth_output = "Le dernier élément de la Liste : " + str(list[-1])

    stringList = ":".join(str(i) for i in list)
    tenth_output = "La Liste transformée en String délimitée par des doubles points : " + str(stringList)

    stringList += ":175"
    eleventh_output = "Le String avec une valeur concaténée" + str(stringList)

    re_list = stringList.split(":")
    last_output = "Le String re-transformé en Liste : " + str(re_list)

    return (first_output + "\n" + second_output + "\n" + third_output + "\n" 
    + fourth_output + "\n" + fifth_output + "\n" + sixth_output + "\n" + seventh_output
    + "\n" + eighth_output + "\n" + ninth_output + "\n" + tenth_output + "\n" 
    + eleventh_output + "\n" + last_output)


# ex 2.6
def return_length_of_lists() :
    carre3 = [[2, 7, 3], [9, 5, 1], [4, 3, 8]]
    carre4 = [[4, 5, 11, 14], [15, 10, 8, 1], [6, 3, 13, 12], [9, 16, 2, 7]]

    output = ("La longueur de carre3 est de " + str(len(carre3)) + " Listes." 
    + "\nLa longueur de carre4 est de " + str(len(carre4)) + " Listes.")

    return output


# ex 2.7
def return_dictionary_operations() : 
    d = {'nom': "Dupuis", 'prenom': "Jacque", 'age': 30}

    d.update({'prenom': "Jacques"})

    keys = d.keys()
    keys_output = "La liste de clés du dictionnaire : " + str(keys)

    values = d.values()
    values_output = "La liste de valeurs du dictionnaire : " + str(values)

    items = d.items()
    items_output = "La liste de objets du dictionnaire : " + str(items)

    jacques_output = str(d.get('prenom')) + " " + str(d.get('nom')) + " a " + str(d.get('age')) + " ans."

    return keys_output + "\n" + values_output + "\n" + items_output + "\n" + jacques_output


# ex 2.8
def return_mon_wed_sun() :

    mon_output = "Lundi : " + return_week_message("lundi")
    wed_output = "Mercredi : " + return_week_message("mercredi")
    sun_output = "Dimanche : " + return_week_message("dimanche")

    return mon_output + "\n" + wed_output + "\n" + sun_output


# ex 2.9

def print_question_numbers_state() :
    def print_number_state_pos_zero_neg_even_odd(number) :
        pos_zero_neg_output = return_number_state_pos_zero_neg(number)
        even_odd_output = return_number_state_even_odd(number)

        return pos_zero_neg_output + " " + even_odd_output
    
    number1_output = "Pour le chiffre 3 : " + str(print_number_state_pos_zero_neg_even_odd(3))
    number2_output = "Pour le chiffre 12 : " + str(print_number_state_pos_zero_neg_even_odd(12))
    number3_output = "Pour le chiffre -33 : " + str(print_number_state_pos_zero_neg_even_odd(-33))
    number4_output = "Pour le chiffre 0 : " + str(print_number_state_pos_zero_neg_even_odd(0))

    return number1_output + "\n" + number2_output + "\n" + number3_output + "\n" + number4_output

