# import helper
# from helper import * --> importing everything from helper is not recommended
from helper import validate_and_execute, user_message

user_input = ""

while user_input != "exit":
    user_input = input(user_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_units_dict = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_units_dict)
    validate_and_execute(days_and_units_dict)

