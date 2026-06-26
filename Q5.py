# Student Database Program

def student_database():
    students = {}

    while True:
        print("\n----- MENU -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({
                    roll: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student added successfully!")

            except ValueError:
                print("Age should be a number.")

        elif choice == "2":
            roll = input("Enter Roll Number to Search: ")

            record = students.get(roll)

            if record:
                print("Student Details:")
                print(record)
            else:
                print("Student not found.")

        elif choice == "3":
            if len(students) == 0:
                print("No student records found.")
            else:
                print("\nAll Student Records:")
                for roll, record in students.items():
                    print("Roll No:", roll)
                    print("Name:", record["Name"])
                    print("Age:", record["Age"])
                    print("City:", record["City"])
                    print()

        elif choice == "4":
            print("Program Ended.")
            break

        else:
            print("Invalid choice. Try again.")


# Main Program
student_database()