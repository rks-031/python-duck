def days_to_units(number_of_days, name_of_unit):
    if name_of_unit == "hours":
        calculation_to_units = 24
    elif name_of_unit == "minutes":
        calculation_to_units = 1440
    elif name_of_unit == "seconds":
        calculation_to_units = 86400
    else:
        return "Unsupported unit. Please use 'hours', 'minutes', or 'seconds'."
    
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}."
    

def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number>0:
            calculated_value = days_to_units(user_input_number, days_and_units_dict["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("Zero is not a valid input. Please enter a positive number of days.")
        else:
            print("Please enter a positive number of days.")
        
    except ValueError:
        print("Please enter a valid number of days. Don't ruin my program.")

user_input = ""

while user_input != "exit":
    user_input = input("Enter the number of days and converstion unit (days:unit)!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_units_dict = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_units_dict)
    validate_and_execute()