employee = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
     }
def add_employee():
    emp_id = int(input("Enter Employee Id: "))
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

    print(f"Employee {name} added successfully.")

def view_employee():
    if not employee:
        print("No employees available. ")
        return

    print("\nEmp ID | Name | Department | Salary")
    print("----------------------------------------")

    for emp_id, data in employee.items():
        print(f"{emp_id:<7} | {data['name']:<10} | {data['age']:<3} | {data['department']:<10} | {data['salary']}")


def serch_employee():
    emp_id = int(input("Enter Employee ID to Search: "))
    if emp_id in employee:
        emp = employee[emp_id]
        print(f"\nFound Employee:\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\nSalary: {emp['salary']}")
    else:
        print("Employee Not Found.")


def main_menu():
    while True:
        print("\n--- Employee Managemaent System---")
        print("1. Add Employee")
        print("2. View All Employee")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employee()
        elif choice == '3':
            serch_employee()
        elif choice == '4':
            print("Thank you")
            break
        else:
            print("Invalid input try again")

main_menu()


