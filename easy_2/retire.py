import datetime

current_age = int(input('How old are you? '))
retirement_age = int(input('At what age would you like to retire? '))

year = datetime.date.today().year
remaining_years = retirement_age - current_age

print(f"It's {year}. You will retire in {year + remaining_years}.\n"
      f"You only have {remaining_years} years of work to go!")