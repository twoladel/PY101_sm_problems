def negative(num):
    try:
        if type(num) != int:
            num = int(num)
        return num if num <= 0 else (num * -1)
    except ValueError:
        return "Please submit an integer type."
    except TypeError:
        return "you messed up."
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

print()
print(negative('23'))
print(negative(45))
print(negative([1]))
print(negative('abc'))

# LS solution with abs()
def negative_num(num):
    return -abs(num)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
    

