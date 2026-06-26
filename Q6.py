import random
import math

numbers = set()

print("Enter 10 numbers:")

while len(numbers) < 10:
    try:
        num = int(input(f"Enter number {len(numbers) + 1}: "))
        numbers.add(num)

    except ValueError:
        print("Please enter a valid number.")

# Convert set into tuple
num_tuple = tuple(numbers)

print("\nUnique Numbers:", numbers)
print("Tuple:", num_tuple)

try:
    # Pick 3 random numbers
    random_numbers = random.sample(num_tuple, 3)
    print("3 Random Numbers:", random_numbers)

    # Square root of sum
    total = sum(num_tuple)
    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Not enough unique numbers to select 3.")

except Exception as e:
    print("Error:", e)