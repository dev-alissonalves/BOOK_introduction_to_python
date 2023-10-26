salary = float(input("What is the salary to be calculated: "))
salary_increase = int(input("What is the percentage increase in salary: (default: 10%): "))
amounts_to_received = salary + (salary * (salary_increase / 100))

print(f"The total amount receivable considered a {salary_increase}% increase is: {amounts_to_received:.2f}")