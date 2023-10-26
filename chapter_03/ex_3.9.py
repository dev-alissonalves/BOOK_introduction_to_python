number_of_days = int(input("Insert numbers of days: (integers only): "))
number_of_hours = float(input("Insert numbers of hours: "))
number_of_seconds = int(input("Insert numbers of seconds: "))

days_in_seconds = (number_of_days * 24) * (60 ** 2)
hours_in_seconds = number_of_hours * 3600
total_seconds = days_in_seconds + hours_in_seconds + number_of_seconds

print(f"The total of seconds is: {total_seconds:.0f}")