number = int(input("Please enter an integer greater than zero: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if operation.casefold() == 's':
    result = sum(range(1, (number + 1)))
    print(f'The sum of the integers between 1 and {number} is {result}.')
elif operation.casefold() == 'p':
    result = 1
    for num in range(1, (number + 1)):
        result *= num
    print(f'The product of the integers between 1 and {number} is {result}.')
else:
    print('Error: enter "s" for sum or "p" for product.')
