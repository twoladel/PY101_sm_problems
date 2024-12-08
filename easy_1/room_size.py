# Get user input for length and width of room
print(
    """Give me the length and width of your room in meters
    and I'll give you the area in square meters
    and square feet.""")
length = int(input("How many meters long is your room? "))
width = int(input("How many meters wide is your room? "))

# Calculate area in meters and feet
sq_meters = length * width
sq_feet = sq_meters * 10.7639

# Print area in sq meters and sq feet
print(f"""Your room's area is {sq_meters:.2f} square meters 
      and {sq_feet:.2f} square feet""")


