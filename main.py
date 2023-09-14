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

# Global variable declarations
num1 = "n" # So the while loop can start
num2 = "n" # So the while loop can start
operator = ""

# Main program
clear_console()
print(art.logo)
# Repeat first number petition until the user types a valid operand
while not is_float(num1):
    str = input("What's the first number?: ")
    if is_float(str):
        num1 = float(str)

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