# def days_to_units(no_of_days):
#     to_seconds = no_of_days * 24 * 60 * 60
#     print(f"There are {to_seconds} seconds in {no_of_days} days!")

    
# user_input = int(input("Enter the number of days\n"))
# days_to_units(user_input)

def days_to_units(no_of_days):
    to_seconds = no_of_days * 24 * 60 * 60
    return (f"There are {to_seconds} seconds in {no_of_days} days!")

user_input = int(input("Enter the number of days\n")) # by defualt input is string, so we convert it to int --> casting
my_var = days_to_units(user_input)
print(my_var)