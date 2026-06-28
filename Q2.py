# Function to analyze a string
# analyze string

def analyze_string(s):
    # Check if the string is empty
    if s == "":
        print("String is empty!")
        return

    # Print length
    print("Length of string:", len(s))

    # Print reverse string
    print("Reverse string:", s[::-1])

    # Count vowels
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    # Print characters with positive and negative index
    print("\nCharacter with Indexes:")
    for i in range(len(s)):
        print("Positive Index:", i,
              "Negative Index:", i - len(s),
              "Character:", s[i])


# Main Program
text = input("Enter a string: ")
analyze_string(text)