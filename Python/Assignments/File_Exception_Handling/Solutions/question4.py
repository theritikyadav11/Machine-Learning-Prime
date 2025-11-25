import json

# Step 1: Create dictionary and save to JSON
cities = {
    "Delhi": 19000000,
    "Mumbai": 21000000,
    "Bengaluru": 12000000
}

with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("Initial cities.json created successfully.\n")

# Step 2: Load the JSON file
with open("cities.json", "r") as f:
    loaded_cities = json.load(f)

# Step 3: Print each city and population
print("Current Cities and Populations:")
for city, population in loaded_cities.items():
    print(f"{city}: {population}")

# Step 4: Ask user for new city and population
new_city = input("\nEnter a new city name: ")
new_population = int(input("Enter its population: "))

# Update dictionary
loaded_cities[new_city] = new_population

# Write updated data back to JSON
with open("cities.json", "w") as f:
    json.dump(loaded_cities, f, indent=4)

print("\nUpdated cities.json saved successfully!")
