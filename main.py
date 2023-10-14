employees = []

while True:
    print("\nEmployee Management System")
    print("*" * 30)
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Increase Salary")
    print("4. Show All Employees")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")
        employees.append({"name": name, "salary": salary})
        print(f"{name} has been added to the employee list. Salary: {salary}")

    elif choice == "2":
        name = input("Enter Employee name to remove: ")
        for employee in employees:
            if employee["name"] == name:
                employees.remove(employee)
                print(f"{name} has been removed from the employee list.")
                break
        else:
            print("Employee not found.")

    elif choice == "3":
        name = input("Enter Employee name to increase salary: ")
        increase_amount = input("Enter the amount to increase salary: ")
        for employee in employees:
            if employee["name"] == name:
                employee["salary"] = str(float(employee["salary"]) + float(increase_amount))
                print(f"Salary for {name} has been increased. New salary: {employee['salary']}")
                break
        else:
            print("Employee not found.")

    elif choice == "4":
        if not employees:
            print("No employees to show.")
        else:
            print("\nEmployee List:")
            print("*" * 30)
            for employee in employees:
                print(f"Name: {employee['name']}, Salary: {employee['salary']}")

    elif choice == "5":
        print("Exiting the Employee Management System.")
        break
