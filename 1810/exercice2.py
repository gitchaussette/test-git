# 3.2.1
# def calculate_sum_prime_numbers(n) :
#     sum_prime_numbers = n * (n + 1) / 2

#     return sum_prime_numbers

print()

def calculate_sum_first_numbers(n) :
    sum = 0

    for i in range(0, n+1) :
        sum += i
        # décommenter pour voir le cheminement
        # print("i : " + str(i))
        # print("sum : " + str(sum))
    
    return sum

print("La somme des premiers nombres de n est : " + str(calculate_sum_first_numbers(5)))
print()

# 3.2.2
# def calculate_sum_even_prime_numbers(n) :
#     sum_even_prime_numbers = (n * (n + 1))

#     return sum_even_prime_numbers

def calculate_sum_even_first_numbers(n) :
    sum = 0

    for i in range(0, n+1) :
        if i % 2 == 0:
            sum += i

    return sum

print("La somme des nombres premiers pairs de n est : " + str(calculate_sum_even_first_numbers(10)))
print()


# 3.2.3
# c'est la même question que celle d'avant ou alors j'ai tout faux depuis tout à l'heure :(


# 3.2.4
# là j'ai fait n'importe quoi du coup ça boucle
# def determine_largest_n(threshold) :
#     number_of_iterations = 0

#     for i in (0, threshold) :
#         print(i)
#         print(threshold)
#         sum_prime_numbers = calculate_sum_prime_numbers(i)
#         while sum_prime_numbers < threshold :
#             number_of_iterations += 1
#             if sum_prime_numbers >= threshold :
#                 number_of_iterations -= 1
#                 return number_of_iterations

#     return number_of_iterations


# ça c'est une boucle infinie.. encore
# def determine_largest_n(max_threshold=15000) :
#     exit_condition = False
#     i = 0

#     while not exit_condition :
#         for i in range(1, i) :
#             print(i)
#             sum = calculate_sum_prime_numbers(i)
#             print(sum)
#             if sum > max_threshold :
#                 exit_condition = True
#                 return i-1

# print("Le plus grand n dont la somme des nombres premiers est inférieure à 15000 : " + str(determine_largest_n(15000)))