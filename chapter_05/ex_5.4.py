import time
number = int(input("Enter the number to be stopped: "))
counter = 0

while counter < number + 1:
    print(counter)
    counter += 1
    time.sleep(1)