def center_of(phrase):
    if len(phrase) % 2 == 0:
        mid_index = int((len(phrase) / 2) - 1)
        return phrase[mid_index:mid_index + 2]
    else:
        mid_index = int(len(phrase) // 2)
        return phrase[mid_index]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True