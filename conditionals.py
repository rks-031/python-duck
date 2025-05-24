calculation_to_units = 24
name_of_unit = "hours"

# def days_to_units(number_of_days):
#     if number_of_days < 0:
#         return "Please enter a positive number of days."
#     return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}."

# using ternary operator
def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}." if number_of_days > 0 else  "Please enter a positive number of days."


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("Please enter a valid number of days. Don't ruin my program.")

user_input = input("Enter the number of days: ")
validate_and_execute()



