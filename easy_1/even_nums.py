# Further exploration add user interaction
print("Hi, I print even numbers.")
start = int(input("Pick an even number for me to start at. "))
stop = int(input("Pick an even number for me to stop at. "))

# Ensure even number
if start % 2 == 1:
    start += 1

# If they want it to print big to small, check before
if start < stop:
    for num in range(start, stop + 1, 2):
        print(num)
else:
    for num in range(start, stop - 1, -2):
        print(num)