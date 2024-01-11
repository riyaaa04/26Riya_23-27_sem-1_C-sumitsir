#Develop a time tracking system for employees with classes for employees,projects, and time entries. Implement methods for logging hours, generatingtimesheets, and calculating overtime.
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def generate_timesheet(self):
        timesheet = {}
        for project in self.projects:
            timesheet[project.name] = sum(entry.hours for entry in project.time_entries)
        return timesheet

    def calculate_overtime(self, weekly_hours_limit=40):
        total_hours = sum(sum(entry.hours for entry in project.time_entries) for project in self.projects)
        overtime_hours = max(0, total_hours - weekly_hours_limit)
        return overtime_hours

class Project:
    def __init__(self, name):
        self.name = name
        self.time_entries = []

    def log_hours(self, date, hours):
        self.time_entries.append(TimeEntry(date, hours))

class TimeEntry:
    def __init__(self, date, hours):
        self.date = date
        self.hours = hours

# Example usage with user input:

# Create Employee
emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
employee = Employee(emp_id, emp_name)

# Create Project
project_name = input("Enter Project Name: ")
project = Project(project_name)

# Log Hours
date = input("Enter Date (YYYY-MM-DD): ")
hours = float(input("Enter Hours Worked: "))
project.log_hours(date, hours)

# Add Project to Employee
employee.add_project(project)

# Generate Timesheet
timesheet = employee.generate_timesheet()
print("Timesheet:")
for project_name, hours_worked in timesheet.items():
    print(f"{project_name}: {hours_worked} hours")

# Calculate Overtime
overtime = employee.calculate_overtime()
print(f"Overtime: {overtime} hours")
