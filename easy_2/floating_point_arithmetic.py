def prompt(message):
    print(f'==> {message}')

def calculate_result(first_num, second_num, operator):
    match operator:
        case '+': return first_num + second_num
        case '-': return first_num - second_num
        case '*': return first_num * second_num
        case '/': return first_num / second_num
        case '//': return first_num // second_num
        case '%': return first_num % second_num
        case '**': return first_num ** second_num

prompt("Enter the first number:")
num1 = float(input())

prompt("Enter the second number:")
num2 = float(input())

for op in ['+', '-', '*', '/', '//', '%', '**']:
    result = calculate_result(num1, num2, op)
    prompt(f"{num1} {op} {num2} = {result}")
