class Company:
    def __init__(self):
        # employee id -> {"name": ..., "department": ..., "salary": ...}
        self.employees = {}
        self.next_emp_id = 1

    def add_employee(self):
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()
        if not name or not department:
            print("Name and department cannot be empty")
            return
        salary = self.get_salary("Enter salary: ")
        if salary is None:
            return
        emp_id = self.next_emp_id
        self.employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary,
        }
        self.next_emp_id += 1
        print(f"Employee added successfully. Employee ID is {emp_id}")

    def show_employees(self):
        print("\nEmployees in company:")
        if not self.employees:
            print("No employees yet")
        for emp_id, info in self.employees.items():
            print(
                f"{emp_id} | {info['name']} | {info['department']} | "
                f"Salary: {info['salary']:.2f}"
            )

    def get_employee(self):
        try:
            emp_id = int(input("Enter employee ID: "))
        except ValueError:
            print("Invalid employee ID")
            return None
        if emp_id not in self.employees:
            print("Employee not found")
            return None
        return emp_id

    def get_salary(self, prompt):
        try:
            salary = float(input(prompt))
        except ValueError:
            print("Invalid amount")
            return None
        if salary <= 0:
            print("Salary must be greater than zero")
            return None
        return salary

    def search_employee(self):
        keyword = input("Enter name or department to search: ").strip().lower()
        found = False
        for emp_id, info in self.employees.items():
            if keyword in info["name"].lower() or keyword in info["department"].lower():
                print(
                    f"{emp_id} | {info['name']} | {info['department']} | "
                    f"Salary: {info['salary']:.2f}"
                )
                found = True
        if not found:
            print("No matching employee found")

    def update_salary(self):
        emp_id = self.get_employee()
        if emp_id is None:
            return
        salary = self.get_salary("Enter new salary: ")
        if salary is None:
            return
        self.employees[emp_id]["salary"] = salary
        print("Salary updated successfully")

    def remove_employee(self):
        emp_id = self.get_employee()
        if emp_id is None:
            return
        removed = self.employees.pop(emp_id)
        print(f"{removed['name']} removed successfully")


company = Company()
while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Remove Employee")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number")
        continue
    if choice == 1:
        company.add_employee()
    elif choice == 2:
        company.show_employees()
    elif choice == 3:
        company.search_employee()
    elif choice == 4:
        company.update_salary()
    elif choice == 5:
        company.remove_employee()
    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid choice")