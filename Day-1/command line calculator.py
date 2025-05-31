def sum():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")
    
def subtract():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"The difference is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def multiply():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"The product is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def divide():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The quotient is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def exponent():
    try:
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = base ** exponent
        print(f"The result of {base} raised to the power of {exponent} is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def modulus():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 % num2
            print(f"The modulus is: {result}")
    except ValueError:
        print("Invalid input, please enter numeric values.")

# function to handle user choice and call the appropriate operation
def operations(user_choice):
    if(user_choice == "1"):
        print("You chose addition")
        sum()
    elif(user_choice == "2"):
        print("You chose subtraction")
        subtract()
    elif(user_choice == "3"):
        print("You chose multiplication")
        multiply()
    elif(user_choice == "4"):
        print("You chose division")
        divide()
    elif(user_choice == "5"):
        print("You chose exponentiation")
        exponent()
    elif(user_choice == "6"):
        print("You chose modulus")
        modulus()
    else:
        print("Invalid choice, please try again.")

# Main function to run the calculator     
def main():
    print("Welcome to the Command Line Calculator!")
    user_choice = 'Y'
    while user_choice == 'y' or user_choice == 'Y':
        print("Please choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Modulus")
        
        user_input = input("Enter your choice (1-6) or 'q' to quit: ")

        if user_input.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        operations(user_input)
        user_choice = input("Do you want to perform another operation? (Y/N): ")

if __name__ == "__main__":
    main()