import time

start = int(input("beginning of the multiplication table: "))
end = int(input("end of multiplication table: "))
table_number = int(input("Enter a value to calculate the table: "))

while start <= end:
    print(table_number, "x", start, "=", table_number * start)
    start += 1
    time.sleep(1)
print("")