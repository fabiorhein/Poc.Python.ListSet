calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validade_and_execute(num_of_days):
    try:

        user_input_number = int(num_of_days)

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a Zero, please enter a valid positive value")
        else:
            print("You entered a negative number, no convertion for you")
    except ValueError:
        print("your input is not number. Don't ruin my program!")




user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days and conversion unit!\n")
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(user_input.split(", ")):
        validade_and_execute(num_of_days_element)


