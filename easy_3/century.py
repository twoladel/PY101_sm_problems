def century(year):
    if year <= 100:
        return ("1st")
    if year % 100 == 0:
        century = year // 100
        return (f"{century}{year_suffix(century)}")
    if year % 100 != 0:
        century = (year // 100) + 1
        return(f"{century}{year_suffix(century)}")

def year_suffix(century):
    if (century % 10 == 1 and century % 100 == 11) or (century % 10 == 2 and century % 100 ==12) or (century % 10 == 3 and century % 100 == 13):
        return 'th'
    elif century % 10 == 1:
        return 'st'
    elif century % 10 == 2:
        return 'nd'
    elif century % 10 == 3:
        return 'rd'
    else:
        return 'th'
    
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True