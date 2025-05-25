import datetime as dt

def time_till_deadline(user_deadline):
    # current date
    current_date = dt.datetime.today()
    # convert user input to date
    deadline_date = dt.datetime.strptime(user_deadline, "%d-%m-%Y")
    # calculate the difference
    delta = deadline_date - current_date
    return delta

user_input = input("Enter your goal and deadline (goal:dd-mm-yyyy)!\n")
input_list = user_input.split(':')

print("You entered:", input_list)

user_goal = input_list[0].strip()
user_deadline = input_list[1].strip()

time = time_till_deadline(user_deadline)

print(f"The time remaining until your goal '{user_goal}' is {time.days} days.")

print("OR")

time_in_hours = int(time.total_seconds()/3600)
print(f"The time remaining until your goal '{user_goal}' is {time_in_hours} hours.")