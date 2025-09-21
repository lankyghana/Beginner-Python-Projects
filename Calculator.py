import math

def add(value1, value2): 
    return value1 + value2

def sub(value1, value2): 
    return value1 - value2

def mul(value1, value2): 
    return value1 * value2

def div(value1, value2): 
    if value2 == 0:
        return "Error: Division by zero is not allowed."
    return value1 / value2

def square(value): 
    return math.pow(value, 2)

print("Select your choice of operation".upper())
choices = "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square"
print(choices)

try:
    operation_choice = int(input("Enter choice (1/2/3/4/5): "))
except ValueError:
    print("Invalid choice. Please enter a number between 1 and 5.")
    exit()

def take_inputs(single_input=False):
    if single_input:
        while True:
            try:
                value = float(input("Enter a number: "))
                return value
            except ValueError:
                print("Please enter a valid number.")
    else:
        while True:
            try:
                value1 = float(input("Enter first number: "))
                value2 = float(input("Enter second number: "))
                return value1, value2
            except ValueError:
                print("Please enter valid numbers.")

if operation_choice == 1:
    value1, value2 = take_inputs()
    print(f"Final result: {add(value1, value2)}")
elif operation_choice == 2:
    value1, value2 = take_inputs()
    print(f"Final result: {sub(value1, value2)}")
elif operation_choice == 3:
    value1, value2 = take_inputs()
    print(f"Final result: {mul(value1, value2)}")
elif operation_choice == 4:
    value1, value2 = take_inputs()
    print(f"Final result: {div(value1, value2)}")
elif operation_choice == 5:
    value = take_inputs(single_input=True)
    print(f"Final result: {square(value)}")
else:
    print("Invalid choice. Please select a valid operation.")