number_1 = float(input("Insert the first number: "))
number_2 = float(input("Insert the second number: "))
number_3 = float(input("Insert the third number: "))

if number_1 > number_2 and number_1 > number_3:
    print(f"The number {number_1} is the biggest!")
    if number_2 > number_3:
        print(f"The number {number_3} is the smallest!")
    else:
        print(f"The number {number_2} is the smallest!")
elif number_2 > number_1 and number_2 > number_3:
    print(f"The number {number_2} is the biggest!")
    if number_1 > number_3:
        print(f"The number {number_3} is the smallest!")
    else:
        print(f"The number {number_1} is the smallest!")
else:
    print(f"The number {number_3} is the biggest!")
    if number_1 > number_2:
        print(f"The number {number_2} is the smallest!")
    else:
        print(f"The number {number_1} is the smallest!")