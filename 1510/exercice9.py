from general.functions_exercise import return_number_state_pos_zero_neg
from general.functions_exercise import return_number_state_even_odd

def print_number_state_pos_zero_neg_even_odd(number) :
    pos_zero_neg_output = return_number_state_pos_zero_neg(number)
    even_odd_output = return_number_state_even_odd(number)

    return pos_zero_neg_output + " " + even_odd_output

print()
print("Pour le chiffre 3 : " + str(print_number_state_pos_zero_neg_even_odd(3)))
print("Pour le chiffre 12 : " + str(print_number_state_pos_zero_neg_even_odd(12)))
print("Pour le chiffre -33 : " + str(print_number_state_pos_zero_neg_even_odd(-33)))
print("Pour le chiffre 0 : " + str(print_number_state_pos_zero_neg_even_odd(0)))
print()