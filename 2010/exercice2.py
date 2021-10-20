int_list = [12, 45, 420, 69, 8, 325, 1]

print()

sum_of_squared_odd_numbers_list = sum(x**2 for x in int_list if x % 2 != 0)

# def return_sum_of_squared_odd_numbers() :
#     sum = 0

#     for x in int_list :
#         if x % 2 != 0 :
#             sum += x**2

#     return sum


# print(return_sum_of_squared_odd_numbers())
print(sum_of_squared_odd_numbers_list)
print()