# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ").strip()
if name == "":
  print("Passenger name is required.")
  exit()
 
distance = float(input("Enter distance (km): "))
if distance < 0:
  print("Invalid distance.")
  exit()
 
passengers = int(input("Enter number of passengers: "))
if passengers <= 0:
      print("Invalid number of passengers")
      exit()
      
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
