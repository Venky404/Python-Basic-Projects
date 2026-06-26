# Lambda function
square = lambda x: x * x

try:
    numbers = list(range(1, 21))

    squares = []

    for num in numbers:
        squares.append(square(num))

    print("Squares of Numbers:")
    print(squares)

    print("\nEven Squares:")

    for value in squares:
        if value % 2 == 0:
            print(value)

except Exception as e:
    print("Error:", e)