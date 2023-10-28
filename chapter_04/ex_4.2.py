speed_car = int(input("What is the speed of the car: "))

if speed_car > 80:
    traffic_fine = speed_car - 80
    print(f"Please reduce speed!\nYou were fined R$ {(traffic_fine * 5.0):.1f} for driving {traffic_fine} KM above the permitted limit.")
else:
    print("You are safe!\nContinue the journey.")