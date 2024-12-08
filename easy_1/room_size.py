# Get user input for feet or meters and then length and width of room.
print("I'll give you the area of your room.")
unit = input("What unit of measurement? Enter f for feet or m for meters: ")
length = float(input("How long is your room? "))
width = float(input("How wide is your room? "))

if unit == 'm':
    # Calculate area in meters and feet, print.
    sq_meters = length * width
    sq_feet = sq_meters * 10.7639
    print(f"Your room's area is {sq_meters:.2f}({sq_feet:.2f})")
elif unit == 'f':
    # Calculate area in feet and meters, print.
    sq_feet = length * width
    sq_meters = sq_feet / 10.7639
    print(f"Your room's area is {sq_feet:.2f} ({sq_meters:.2f})")


