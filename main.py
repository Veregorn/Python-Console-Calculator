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

# Function that receives a number to operate with and ask the user for the operator and the second number
def calculate(num1):

    # Variable declarations
    num2 = "n" # So the while loop can start
    operator = "" # So the while loop can start

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

    # Return the result
    return result

# Main program loop
while continue_calculating == "n":
    # Clear console and print the logo
    clear_console()
    print(art.logo)

    # Variable declarations
    num1 = "n" # So the while loop can start

    # Repeat first number petition until the user types a valid operand
    while not is_float(num1):
        str = input("What's the first number?: ")
        if is_float(str):
            num1 = float(str)

    # Call the calculate function
    result = calculate(num1)

    # Ask the user if he wants to continue calculating, start a new one or exit the program
    continue_calculating = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type something else to exit: ").lower()

    # If the user wants to continue calculating, enter the loop
    while continue_calculating == "y":
        result2 = calculate(result)
        continue_calculating = input(f"Type 'y' to continue calculating with {result2}, type 'n' to start a new calculation or type something else to exit: ").lower()
        if continue_calculating == "y":
            result = result2 # So the next calculation starts with the result of the previous one