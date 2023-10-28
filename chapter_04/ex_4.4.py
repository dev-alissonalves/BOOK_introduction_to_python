employee_salary = float(input("What is the employee's salary: "))

if employee_salary > 1250:
    print(f"The {employee_salary} salary will have a (10%) increase.\nThe total with increase is {employee_salary + (employee_salary * 0.10)}")
else:
    print(f"The {employee_salary} salary will have a (15%) increase.\nThe total with increase is {employee_salary + (employee_salary * 0.15)}")