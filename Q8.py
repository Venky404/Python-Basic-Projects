# Employee Class

class Employee:

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])


# Dictionary to store employees
employees = {}

# Add 3 employees
for i in range(3):
    print(f"\nEnter details of Employee {i + 1}")

    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    emp = Employee(emp_id, name, department, salary)

    employees[emp_id] = emp

# Display all employees
print("\n----- Employee Details -----")

for emp in employees.values():
    emp.show_details()