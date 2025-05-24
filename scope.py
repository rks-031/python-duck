name_of_unit = "hours"

def days_to_units(no_of_days, custom_message):
    print(f"There are {to_seconds} seconds in {no_of_days} days!")
    print(custom_message)

def scope_check():
    print(name_of_unit) # valid as name_of_unit is global
    print(custom_message) # invalid as custom_message has a local scope in days_to_unit fn
    

scope_check()

# Error message:

# Traceback (most recent call last):
#   File "/home/jdoodle.py", line 32, in <module>
#     scpe_check()
#     ^^^^^^^^^^
# NameError: name 'scpe_check' is not defined. Did you mean: 'scope_check'?