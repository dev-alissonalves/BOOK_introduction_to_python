import time
counter = 1
table_number = int(input("Enter a value to calculate the table: "))

while counter <= 10:
    print(table_number, "x", counter, "=", table_number * counter)
    counter += 1
    time.sleep(1)