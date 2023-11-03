distance_km = float(input("What is the distance to be covered in kilometers? "))

if distance_km > 200:
    print(f"The distance to be covered is {distance_km} kilometers and the ticket price is $ {distance_km * 0.45}")
else:
    print(f"The distance to be covered is {distance_km} kilometers and the ticket price is $ {distance_km * 0.50}")