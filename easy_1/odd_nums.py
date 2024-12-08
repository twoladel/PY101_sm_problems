# Further exploration add user interaction
print("Hi, I print odd numbers.")
start = int(input("What number should I start at? "))
stop = int(input("What number should I stop at? "))

for num in range(start, stop + 1, 2):
    print(num)