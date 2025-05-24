# def days_to_units():
#     print(f"There are {to_seconds} seconds in {days} days!")
#     print("End of function days_to_units")
    

# days = 20
# to_seconds = 20*24*60*60
# days_to_units()

# using parameters in functions
# def days_to_units(no_of_days):
#     print(f"There are {to_seconds} seconds in {no_of_days} days!")
    
# to_seconds = 20*24*60*60
# days_to_units(20)

def days_to_units(no_of_days, custom_message):
    print(f"There are {to_seconds} seconds in {no_of_days} days!")
    print(custom_message)
    
to_seconds = 20*24*60*60
days_to_units(20,"End of function days_to_units")