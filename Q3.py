# Function to manage marks

def manage_marks():
    marks = []

    print("Enter marks of 5 subjects:")

    while len(marks) < 5:
        try:
            mark = float(input(f"Subject {len(marks)+1}: "))
            marks.append(mark)

        except ValueError:
            print("Please enter a valid number!")

    # Average
    average = sum(marks) / len(marks)

    print("\nMarks List:", marks)
    print("Average Marks:", average)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    # Sort in descending order
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)


# Main Program
manage_marks()