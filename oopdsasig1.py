class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

class HRDepartment:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, emp_id, emp_name, emp_salary):
        new_employee = Employee(emp_id, emp_name, emp_salary)
        self.employee_list.append(new_employee)

    def find_employee_by_id(self, emp_id):
        for employee in self.employee_list:
            if employee.emp_id == emp_id:
                return employee
        return None

    def display_all_employees(self):
        print("Employee Details:")
        for employee in self.employee_list:
            print(f"ID: {employee.emp_id}, Name: {employee.emp_name}, Salary: {employee.emp_salary}")

# Create an instance of the HRDepartment class
hr_dept = HRDepartment()

# Add employees
hr_dept.add_employee(1, "Jacaranda wangari", 52000)
hr_dept.add_employee(2, "fayum Smith", 67000)
hr_dept.add_employee(3, "niko omalana", 53000)

# Display all employees
hr_dept.display_all_employees()

# Find an employee by ID
search_id = 2
found_employee = hr_dept.find_employee_by_id(search_id)
if found_employee:
    print(f"Employee found - ID: {found_employee.emp_id}, Name: {found_employee.emp_name}, Salary: {found_employee.emp_salary}")
else:
    print(f"Employee with ID {search_id} not found.")
