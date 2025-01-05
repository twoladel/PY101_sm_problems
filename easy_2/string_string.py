def stringy(length):
    result = ['1' if i % 2 == 0 else '0' for i in range (length)]
    return ''.join(result)
    

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
