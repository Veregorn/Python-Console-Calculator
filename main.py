# Files needed: art.py. Library: os
import art
import os

# Clear console function (works on Windows and Linux)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function that test if the input is a number
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
    
# Function that test if a string is a valid operator
def is_valid_operator(str):
    if str == "+" or str == "-" or str == "*" or str == "/":
        return True
    else:
        return False
    
# Function that add two numbers
def add(num1, num2):
    return num1 + num2

# Function that substract two numbers
def substract(num1, num2):
    return num1 - num2

# Function that multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function that divide two numbers
def divide(num1, num2):
    return num1 / num2

# Global variable declarations
result = 0
continue_calculating = "n"
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# Main program loop
while continue_calculating == "n":
    # Clear console and print the logo
    clear_console()
    print(art.logo)

    # Variable declarations
    num1 = "n" # So the while loop can start
    num2 = "n" # So the while loop can start
    operator = "" # So the while loop can start

    # Repeat first number petition until the user types a valid operand
    while not is_float(num1):
        str = input("What's the first number?: ")
        if is_float(str):
            num1 = float(str)

    # Define the variable that will control the continue calculating while loop
    continue_calculating = "y"

    # Loop to continue calculating with the result of the previous calculation
    while continue_calculating == "y":
        # Repeat operator petition until the user types a valid one
        while not is_valid_operator(operator):
            operator = input("Pick an operation (+ - * /): ")

        # Repeat second number petition until the user types a valid operand
        while not is_float(num2):
            str = input("What's the second number?: ")
            if is_float(str):
                if str == "0" and operator == "/":
                    print("You can't divide by zero! Try with another number.")
                else:
                    num2 = float(str)

        # Calculate the result
        result = operations[operator](num1, num2) # Wow, this is cool!

        # Print the result
        print(f"{num1} {operator} {num2} = {result}")

        # Reset the variables
        continue_calculating = ""
        operator = ""
        num2 = "n"

        # Ask the user if he wants to continue calculating, start a new one or exit the program
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type something else to exit: ").lower()

        # If the user wants to continue calculating, num1 will be the result of the previous calculation
        if continue_calculating == "y":
            num1 = result