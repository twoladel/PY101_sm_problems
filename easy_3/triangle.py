def right_triangle(size):
    for i in range (size):
        print(f"{' ' * (size - (i + 1))} {'*' * (i + 1)}")

right_triangle(5)
right_triangle(9)