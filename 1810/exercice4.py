
print()

def calculate_x_value(x) :
    if x % 9 == 0 :
        y = x / 9
    else :
        y = x - 9

    return "y = " + str(y)

def return_list_x_values() :
    first_output = "Value for x=27 : " + str(calculate_x_value(27))
    second_output = "Value for x=3339 : " + str(calculate_x_value(3339))
    third_output = "Value for x=2345 : " + str(calculate_x_value(2345))
    fourth_output = "Value for x=666 : " + str(calculate_x_value(666))

    return first_output + "\n" + second_output + "\n" + third_output + "\n" + fourth_output

print(return_list_x_values())
print()