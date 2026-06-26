import math

try:
    sentence = input("Enter a sentence: ")

    # Convert sentence into words
    words = sentence.split()

    # Store unique words in a set
    unique_words = set(words)

    # Sort the words
    sorted_words = sorted(unique_words)

    print("\nUnique Words:")
    for word in sorted_words:
        print(word)

    # Square of total unique words
    total = len(unique_words)
    result = math.pow(total, 2)

    print("\nTotal Unique Words:", total)
    print("Square of Total Unique Words:", result)

except Exception as e:
    print("Error:", e)