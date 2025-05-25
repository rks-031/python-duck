print("Enter how many times you want to repeat the task:")
number_of_times = int(input())

print(f"Enter the number of days {number_of_times} times:")

days_set = set() # Using a set to avoid duplicates

for i in range(number_of_times):
    user_input = input()
    days_set.add(user_input)


calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}." if number_of_days > 0 else  "Please enter a positive number of days."
    

def validate_and_execute(no_of_days):
    try:
        no_of_days = int(no_of_days)
        if no_of_days > 0:
            calculated_value = days_to_units(no_of_days)
            print(calculated_value)
        elif no_of_days == 0:
            print("Zero is not a valid input. Please enter a positive number of days.")
        else:
            print("Please enter a valid positive number of days.")
        
    except:
        print("Please enter a valid number of days. Don't ruin my program.")

for ele in sorted(days_set): # sorting to ensure consistent order
    no_of_days = ele
    validate_and_execute(no_of_days)

# insert an element into the set: set.add(element)
# remove an element from the set: set.remove(element)