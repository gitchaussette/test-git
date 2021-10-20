animal_list = ["aigle", "boule", "animal", "écrevisse", "fourmisse", "paon", "panda", "ours"]
length_list = []
n = 4

print()

n_length_words_list = [x for x in animal_list if len(x) == n]

# def return_list_of_n_length_words_from_list(list) :
#     n = 4

#     for x in list :
#         if len(x) == n :
#             length_list.append(x)
    
#     return length_list

# print(return_list_of_n_length_words_from_list(animal_list))
print(n_length_words_list)
print()