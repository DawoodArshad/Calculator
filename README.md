# Calculator
**Simple Calculator:**
<br>
This is a simple command-line calculator implemented in Python. It provides basic arithmetic operations: addition, subtraction, multiplication, and division. The user can choose an operation, input two numbers, and receive the result.

Features
Addition: Adds two numbers.
Subtraction: Subtracts the second number from the first.
Multiplication: Multiplies two numbers.
Division: Divides the first number by the second, with error handling for division by zero.
Usage
To run the program the user have to Choose an operation: When prompted, enter:
1 for addition
2 for subtraction
3 for multiplication
4 for division
q to exit the program
Input numbers: After selecting an operation, the user will give two numbers when asked.
**Example:**
choose option:
1. addition
2. subtraction
3. multiplication
4. division
press 1,2,3,4 or q for exiting: 1
tell first number: 5
tell second number: 3
Result: 8.0
Error Handling
If the user attempts to divide by zero, the program will output an error message: "Error. Can’t divide by zero."
If the user inputs a non-numeric value, the program will prompt them to enter a valid number.
Code Structure
python

Run

def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return ("Error. Can’t divide by zero.")
    return x / y
Main Loop
The program validates user input and re-requests entry when an invalid value is provided.
