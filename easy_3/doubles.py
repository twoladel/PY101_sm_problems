def twice(number):
    number = str(number)
    digits = len(number)
    if digits % 2 == 0:
        slice_end = digits // 2
        if number[:slice_end] == number[slice_end:]:
            return int(number)
        else:
            return int(number) * 2
    else:
        return int(number) * 2
    

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True