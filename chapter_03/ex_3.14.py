trip_distance = float(input("How many km are traveled: "))
days_vehicle_rented = int(input("How many days was the vehicle rented: "))

print("\n ====== META AI TRAVEL AND SERVICES ====== \n")

price_to_pay = (days_vehicle_rented * 60) + (trip_distance * 0.15)

print(f"The price to pay is: {price_to_pay}\n")