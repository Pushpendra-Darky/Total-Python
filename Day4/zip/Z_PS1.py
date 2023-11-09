capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

zip_combo = list(zip(capitals,countries))

for city,country in zip_combo:
    print(f"The capital of {country} is {city}")
