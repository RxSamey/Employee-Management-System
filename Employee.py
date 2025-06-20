employee = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employee:
        print("Employee already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print(f" Employee '{name}' added successfully.")

def view_employee():
    if not employee:
        print("No employees available.")
        return

    print(f"\n{'Emp ID':<8} | {'Name':<10} | {'Age':<3} | {'Department':<10} | {'Salary'}")
    print("-" * 55)

    for emp_id, data in employee.items():
        print(f"{emp_id:<8} | {data['name']:<10} | {data['age']:<3} | {data['department']:<10} | {data['salary']}")

def search_employee():
    emp_id = int(input("Enter Employee ID to Search: "))
    if emp_id in employee:
        emp = employee[emp_id]
        print(f"\n Found Employee:")
        print(f"Name      : {emp['name']}")
        print(f"Age       : {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary    : {emp['salary']}")
    else:
        print(" Employee Not Found.")

def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employee()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print(" Thank you for using the system.")
            break
        else:
            print(" Invalid input. Please try again.")


main_menu()
