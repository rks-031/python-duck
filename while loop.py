calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}." if number_of_days > 0 else  "Please enter a positive number of days."
    

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number>0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("Zero is not a valid input. Please enter a positive number of days.")
        else:
            print("Please enter a positive number of days.")
        
    except ValueError:
        print("Please enter a valid number of days. Don't ruin my program.")

# while True:
#     user_input = input("Enter the number of days: ")
#     validate_and_execute()

user_input = ""

while user_input != "exit":
    user_input = input("Enter the number of days: ")
    validate_and_execute()