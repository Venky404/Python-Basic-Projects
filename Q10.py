import math
import random
from datetime import datetime

# Dictionary to store history
history = {}


# Function for Basic Arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = num1 + num2
            operation = "Addition"

        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"

        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
            operation = "Division"

        else:
            print("Invalid choice!")
            return

        print("Result:", result)

        time = str(datetime.now())
        history[time] = f"{operation}: {result}"

    except ValueError:
        print("Please enter valid numbers.")


# Function for Scientific Calculations
def scientific_calculation():
    try:
        num = float(input("Enter a number: "))

        print("\nSquare Root:", math.sqrt(num))
        print("Square:", math.pow(num, 2))
        print("Factorial:", math.factorial(int(num)))

        time = str(datetime.now())
        history[time] = f"Scientific Calculation on {num}"

    except ValueError:
        print("Invalid input!")


# Function for Random Numbers
def random_numbers():
    nums = []

    for i in range(5):
        nums.append(random.randint(1, 100))

    print("Random Numbers:", nums)

    time = str(datetime.now())
    history[time] = f"Random Numbers: {nums}"


# Function to View History
def view_history():
    if len(history) == 0:
        print("No history found.")
    else:
        print("\n----- History -----")
        for key, value in history.items():
            print(key, "->", value)


# Main Menu
while True:

    print("\n===== Smart Calculator & Data Manager =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        basic_arithmetic()

    elif choice == "2":
        scientific_calculation()

    elif choice == "3":
        random_numbers()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice! Please try again.")