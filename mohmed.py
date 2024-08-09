employees = []

while True:
    print("enter your choice ")
    print("1) Add new employee")
    print("2) Print all employees")
    print("3) Delete by age")
    print("4) Update Salary by name")
    print("5) End the program")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        employees.append({"name": name, "age": age, "salary": salary})
        print("Employee added successfully!")

    elif choice == '2':
        if not employees:
            print("No employees in the list.")
        else:
            for employee in employees:
                print(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}")

    elif choice == '3':
        age_to_delete = int(input("Enter age of employee to delete: "))
        employees = [emp for emp in employees if emp['age'] != age_to_delete]
        print(f"Employees with age {age_to_delete} deleted.")

    elif choice == '4':
        name_to_update = input("Enter name of employee to update salary: ")
        new_salary = float(input("Enter new salary: "))
        for i, employee in enumerate(employees):
            if employee['name'] == name_to_update:
                employees[i]['salary'] = new_salary
                print("Salary updated successfully!")
                break
        else:
            print("Employee not found.")

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")