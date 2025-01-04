import random

def prompt(message):
    print(f'==> {message}')

def output_person_age(age_arg, name):
    prompt(f'{name} is {age_arg} years old!')

def main():
    prompt("What is your name?")
    name = input()
    if not name:
        name = 'Teddy'
    age = random.randint(20, 100)
    
    output_person_age(age, name)

main()
