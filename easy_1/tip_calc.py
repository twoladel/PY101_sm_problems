# inputs: prompt user for bill total and tip % on seperate lines
# inputs should get converted to floats
# must divide tip by 100 to convert for calculation
# add calculated tip to original bill
# output: tip amount and total bill with tip on seperate lines
# output should have an empty new line before output response.
# format output to two decimals

'''mental model: a restaurant guest should be able to enter the total of a bill
 and the percent they want to tip and get the tip and new total.''' 

''' example 1: What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00'''

''' example 2: What is the bill? 250
What is the tip percentage? 18

The tip is $45.00
The total is $295.00'''

''' example 3: What is the bill? 145.58
What is the tip percentage? 27

The tip is $39.31
The total is $184.89'''

bill = float(input("What is the bill? "))
tip_percent = float(input("What is the tip percentage? "))

tip = bill * (tip_percent / 100)
total = bill + tip

print()
print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")

